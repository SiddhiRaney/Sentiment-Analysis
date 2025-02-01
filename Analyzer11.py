import nltk
import textwrap
import re
from typing import Dict, Any
from transformers import pipeline

# Initialize Hugging Face sentiment analysis pipeline
sentiment_analysis_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(comment: str) -> Dict[str, Any]:
    try:
        # Get sentiment scores using Hugging Face model
        sentiment_result = sentiment_analysis_pipeline(comment)[0]
        label = sentiment_result['label']
        score = sentiment_result['score']

        # Determine sentiment, tone, and sarcasm
        sentiment = determine_sentiment(label)
        tone = determine_tone(label, score)
        sarcasm = detect_sarcasm(comment, label)
        
        return {
            "sentiment": sentiment,
            "tone": tone,
            "sarcasm": sarcasm,
            "score": {"label": label, "score": score},
        }
    except Exception as e:
        return {"error": str(e)}

def determine_sentiment(label: str) -> str:
    """
    Determine the overall sentiment based on the label (positive/negative).
    
    Args:
        label (str): The sentiment label ('POSITIVE' or 'NEGATIVE').
        
    Returns:
        str: The overall sentiment.
    """
    if label == 'POSITIVE':
        return 'Positive'
    elif label == 'NEGATIVE':
        return 'Negative'
    return 'Neutral'

def determine_tone(label: str, score: float) -> str:
    """
    Determine the tone based on sentiment label and score.
    
    Args:
        label (str): Sentiment label ('POSITIVE' or 'NEGATIVE').
        score (float): The confidence score of the sentiment.
        
    Returns:
        str: The tone of the comment.
    """
    if label == 'POSITIVE' and score > 0.9:
        return 'Excited'
    elif label == 'NEGATIVE' and score > 0.9:
        return 'Angry'
    return 'Neutral'

def detect_sarcasm(comment: str, label: str) -> str:
    sarcastic_keywords = ["not", "sure", "yeah right", "totally", "as if"]
    sarcastic_patterns = [r"yeah,? right", r"totally\s.*", r"as if"]
    comment_lower = comment.lower()

    if any(keyword in comment_lower for keyword in sarcastic_keywords):
        return 'Sarcastic'
    if any(re.search(pattern, comment_lower) for pattern in sarcastic_patterns):
        return 'Sarcastic'
    return 'Not Sarcastic'

def display_results(comment: str, result: Dict[str, Any]) -> None:
    """
    Display sentiment analysis results in a clean and readable format.
    
    Args:
        comment (str): The input comment.
        result (Dict[str, Any]): The result dictionary from sentiment analysis.
    """
    print("\n" + "-" * 50)
    print(f"Comment:\n{textwrap.fill(comment, width=50)}")
    print(f"General Sentiment: {result['sentiment']}")
    print(f"Tone: {result['tone']}")
    print(f"Sarcasm Detection: {result['sarcasm']}")
    print("Score Breakdown:")
    for key, value in result['score'].items():
        print(f"  {key.capitalize()}: {value:.2f}")
    print("-" * 50 + "\n")

def main() -> None:
    print("Welcome to the Sentiment Analysis Tool!")
    while True:
        try:
            comment = input("Enter a comment (or type 'exit' to quit): ").strip()
            
            if comment.lower() == 'exit':
                print("Exiting the program...")
                break

            if not comment:
                print("Error: Please enter a valid comment!")
                continue

            result = analyze_sentiment(comment)

            if "error" in result:
                print(f"Error: {result['error']}")
            else:
                display_results(comment, result)

        except KeyboardInterrupt:
            print("\nExiting the program...")
            break

# Run the program
if __name__ == "__main__":
    main()
