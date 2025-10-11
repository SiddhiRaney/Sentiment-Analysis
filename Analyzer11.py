import re
import textwrap
from typing import Dict, Any
from functools import lru_cache

# Try importing transformers safely
try:
    from transformers import pipeline
except ImportError:
    pipeline = None

# Pre-compiled sarcasm regex patterns
SARCASM_PATTERNS = (
    re.compile(r"yeah,? right", re.IGNORECASE),
    re.compile(r"totally\s.*", re.IGNORECASE),
    re.compile(r"as if", re.IGNORECASE),
)

@lru_cache(maxsize=1)
def get_sentiment_pipeline():
    """Load sentiment analysis model only once."""
    if pipeline is None:
        raise ImportError("Transformers is not installed. Run `pip install transformers`.")
    return pipeline("sentiment-analysis")

def analyze_sentiment(comment: str) -> Dict[str, Any]:
    """Analyze sentiment, tone, and sarcasm in a comment."""
    if not comment:
        return {"error": "Empty input provided."}

    try:
        analysis = get_sentiment_pipeline()(comment)[0]
        label, score = analysis["label"], round(analysis["score"], 2)

        sentiment = "Positive" if label.upper() == "POSITIVE" else "Negative"
        tone = (
            "Excited" if score > 0.9 and sentiment == "Positive"
            else "Angry" if score > 0.9 and sentiment == "Negative"
            else "Neutral"
        )
        sarcasm = "Sarcastic" if any(p.search(comment) for p in SARCASM_PATTERNS) else "Not Sarcastic"

        return {
            "sentiment": sentiment,
            "tone": tone,
            "sarcasm": sarcasm,
            "score": {"label": label, "score": score},
        }

    except Exception as e:
        return {"error": str(e)}


def display_results(comment: str, result: Dict[str, Any]) -> None:
        """Pretty print results in a formatted manner."""
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
        if comment.lower() == "exit":
            print("Exiting...")
            break

        result = analyze_sentiment(comment)
        display_results(comment, result)


if __name__ == "__main__":
    main()
