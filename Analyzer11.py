import re
import textwrap
from typing import Dict, Any
from transformers import pipeline

# Pre-compiled sarcasm regex patterns
SARCASM_PATTERNS = [
    re.compile(r"yeah,? right", re.IGNORECASE),
    re.compile(r"totally\s.*", re.IGNORECASE),
    re.compile(r"as if", re.IGNORECASE),
]

# Lazy load pipeline (singleton pattern)
_sentiment_pipeline = None
def get_sentiment_pipeline():
    global _sentiment_pipeline
    if _sentiment_pipeline is None:
        _sentiment_pipeline = pipeline("sentiment-analysis")
    return _sentiment_pipeline


def analyze_sentiment(comment: str) -> Dict[str, Any]:
    """Analyze sentiment, tone, and sarcasm in a comment."""
    try:
        result = get_sentiment_pipeline()(comment)[0]
        label, score = result["label"], result["score"]

        # Sentiment mapping
        sentiment = "Positive" if label.upper() == "POSITIVE" else "Negative"

        # Tone mapping (use thresholds for clarity)
        if sentiment == "Positive" and score > 0.9:
            tone = "Excited"
        elif sentiment == "Negative" and score > 0.9:
            tone = "Angry"
        else:
            tone = "Neutral"

        # Sarcasm detection
        sarcasm = "Sarcastic" if any(p.search(comment) for p in SARCASM_PATTERNS) else "Not Sarcastic"

        return {
            "sentiment": sentiment,
            "tone": tone,
            "sarcasm": sarcasm,
            "score": {"label": label, "score": round(score, 2)},
        }

    except Exception as e:
        return {"error": str(e)}


def display_results(comment: str, result: Dict[str, Any]) -> None:
    """Pretty print results."""
    print("\n" + "-" * 50)
    print("Comment:\n" + textwrap.fill(comment, width=50) + "\n")

    for key, value in result.items():
        if isinstance(value, dict):
            print("Score Breakdown:")
            for sub_k, sub_v in value.items():
                print(f"  {sub_k.capitalize()}: {sub_v}")
        else:
            print(f"{key.capitalize()}: {value}")
    print("-" * 50 + "\n")


def main() -> None:
    """Interactive CLI for sentiment analysis."""
    print("Welcome to the Sentiment Analysis Tool!")
    while True:
        comment = input("Enter a comment (or type 'exit' to quit): ").strip()
        if not comment:
            print("⚠️ Please enter a valid comment.")
            continue
        if comment.lower() == "exit":
            print("Exiting...")
            break

        result = analyze_sentiment(comment)
        display_results(comment, result)


if __name__ == "__main__":
    main()
