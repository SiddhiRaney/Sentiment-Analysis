import re
import textwrap
from typing import Dict, Any
from transformers import pipeline

# Pre-compiled regex patterns for basic sarcasm detection
SARCASM_PATTERNS = [
    re.compile(r"yeah,? right", re.IGNORECASE),
    re.compile(r"totally\s.*", re.IGNORECASE),
    re.compile(r"as if", re.IGNORECASE),
]

# Lazy load Hugging Face sentiment pipeline
_sentiment_pipeline = None
def get_pipeline():
    global _sentiment_pipeline
    if _sentiment_pipeline is None:
        _sentiment_pipeline = pipeline("sentiment-analysis")
    return _sentiment_pipeline


def analyze_sentiment(comment: str) -> Dict[str, Any]:
    """
    Analyze a comment to determine sentiment, tone, and basic sarcasm.
    """
    try:
        # Run the sentiment analysis model
        result = get_pipeline()(comment)[0]
        label, score = result["label"], result["score"]

        # Sentiment mapping
        sentiment = "Positive" if label == "POSITIVE" else "Negative"

        # Tone mapping
        if score > 0.9:
            tone = "Excited" if sentiment == "Positive" else "Angry"
        else:
            tone = "Neutral"

        # Sarcasm detection
        sarcasm = (
            "Sarcastic"
            if any(p.search(comment) for p in SARCASM_PATTERNS)
            else "Not Sarcastic"
        )

        return {
            "sentiment": sentiment,
            "tone": tone,
            "sarcasm": sarcasm,
            "score": {"label": label, "score": round(score, 2)},
        }

    except Exception as e:
        return {"error": str(e)}


def display_results(comment: str, result: Dict[str, Any]) -> None:
    """
    Nicely print the analysis results to the console.
    """
    print("\n" + "-" * 50)
    print("Comment:")
    print(textwrap.fill(comment, width=50), "\n")

    for key, value in result.items():
        if isinstance(value, dict):
            print("Score Breakdown:")
            for sub_key, sub_value in value.items():
                print(f"  {sub_key.capitalize()}: {sub_value}")
        else:
            print(f"{key.capitalize()}: {value}")
    print("-" * 50 + "\n")


def main() -> None:
    """Entry point for the sentiment analysis tool."""
    print("Welcome to the Sentiment Analysis Tool!")
    while True:
        comment = input("Enter a comment (or type 'exit' to quit): ").strip()
        if comment.lower() == "exit":
            print("Exiting the program...")
            break
        if not comment:
            print
