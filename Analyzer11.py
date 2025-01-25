import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import textwrap
import re
from typing import Dict, Any

# Initialize SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(comment: str) -> Dict[str, Any]:
   
    try:
        # Get sentiment scores
        sentiment_scores = sia.polarity_scores(comment)
        compound = sentiment_scores['compound']
        
        # Determine sentiment, tone, and sarcasm
        sentiment = determine_sentiment(compound)
        tone = determine_tone(sentiment_scores)
        sarcasm = detect_sarcasm(comment, sentiment_scores)
        
        return {
            "sentiment": sentiment,
            "tone": tone,
            "sarcasm": sarcasm,
            "scores": sentiment_scores,
        }
    except Exception as e:
        return {"error": str(e)}

def determine_sentiment(compound: float) -> str:
    """
    Determine the overall sentiment based on the compound score.
    
    Args:
        compound (float): The compound score from sentiment analysis.
        
    Returns:
        str: The overall sentiment (Positive, Negative, or Neutral).
    """
    if compound >= 0.05:
        return 'Positive'
    elif compound <= -0.05:
        return 'Negative'
    return 'Neutral'

def determine_tone(scores: Dict[str, float]) -> str:
    """
    Determine the tone based on individual sentiment scores.
    
    Args:
        scores (Dict[str, float]): A dictionary of sentiment scores (pos, neg, neu).
        
    Returns:
        str: The tone of the comment.
    """
    pos, neg, neu = scores['pos'], scores['neg'], scores['neu']
    
    if pos > 0.7:
        return 'Excited'
    elif neg > 0.7:
        return 'Angry'
    elif neu > 0.9:
        return 'Calm'
    elif pos > neg:
        return 'Happy'
    elif neg > pos:
        return 'Sad'
    return 'Mixed'

def detect_sarcasm(comment: str, scores: Dict[str, float]) -> str:
   
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
    for key, value in result['scores'].items():
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
