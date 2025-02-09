import re
import textwrap
from typing import Dict, Any
from transformers import pipeline

# Initialize Hugging Face sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(comment: str) -> Dict[str, Any]:
    try:
        result = sentiment_pipeline(comment)[0]
        label, score = result['label'], result['score']
        return {
            "sentiment": determine_sentiment(label),
            "tone": determine_tone(label, score),
            "sarcasm": detect_sarcasm(comment),
            "score": {"label": label, "score": round(score, 2)},
        }
    except Exception as e:
        return {"error": str(e)}

def determine_sentiment(label: str) -> str:
    return "Positive" if label == "POSITIVE" else "Negative"

def determine_tone(label: str, score: float) -> str:
    if score > 0.9:
        return "Excited" if label == "POSITIVE" else "Angry"
    return "Neutral"

def detect_sarcasm(comment: str) -> str:
    sarcasm_patterns = [r"yeah,? right", r"totally\s.*", r"as if"]
    return "Sarcastic" if any(re.search(pattern, comment.lower()) for pattern in sarcasm_patterns) else "Not Sarcastic"

def display_results(comment: str, result: Dict[str, Any]) -> None:
    print("\n" + "-" * 50)
    print(f"Comment:\n{textwrap.fill(comment, width=50)}")
    for key, value in result.items():
        if isinstance(value, dict):
            print("Score Breakdown:")
            for sub_key, sub_value in value.items():
                print(f"  {sub_key.capitalize()}: {sub_value}")
        else:
            print(f"{key.capitalize()}: {value}")
    print("-" * 50 + "\n")

def main() -> None:
    print("Welcome to the Sentiment Analysis Tool!")
    while True:
        comment = input("Enter a comment (or type 'exit' to quit): ").strip()
        if comment.lower() == 'exit':
            print("Exiting the program...")
            break
        if not comment:
            print("Error: Please enter a valid comment!")
            continue
        result = analyze_sentiment(comment)
        print(f"Error: {result['error']}") if "error" in result else display_results(comment, result)

if __name__ == "__main__":
    main()
