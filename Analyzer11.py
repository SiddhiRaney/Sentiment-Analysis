import re
import textwrap
from typing import Dict, Any
from transformers import pipeline

# Initialize Hugging Face sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Pre-compiled regex patterns for sarcasm detection
sarcasm_patterns = [re.compile(pat, re.IGNORECASE) for pat in [r"yeah,? right", r"totally\s.*", r"as if"]]

def analyze_sentiment(comment: str) -> Dict[str, Any]:
    try:
        result = sentiment_pipeline(comment)[0]
        label = result['label']
        score = result['score']
        return {
            "sentiment": "Positive" if label == "POSITIVE" else "Negative",
            "tone": "Excited" if label == "POSITIVE" and score > 0.9 else "Angry" if label == "NEGATIVE" and score > 0.9 else "Neutral",
            "sarcasm": "Sarcastic" if any(p.search(comment) for p in sarcasm_patterns) else "Not Sarcastic",
            "score": {"label": label, "score": round(score, 2)},
        }
    except Exception as e:
        return {"error": str(e)}

def display_results(comment: str, result: Dict[str, Any]) -> None:
    print("\n" + "-" * 50)
    print("Comment:")
    print(textwrap.fill(comment, width=50))
    print()
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
        comment = input("Enter a comment (or type 'exit' to quit): ")
        if comment.strip().lower() == 'exit':
            print("Exiting the program...")
            break
        if not comment.strip():
            print("Error: Please enter a valid comment!")
            continue
        result = analyze_sentiment(comment)
        if "error" in result:
            print(f"Error: {result['error']}")
        else:
            display_results(comment, result)

if __name__ == "__main__":
    main()
