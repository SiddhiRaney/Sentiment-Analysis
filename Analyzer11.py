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

# Lazy load sentiment pipeline
_sentiment = None
def get_sentiment():
    global _sentiment
    if _sentiment is None:
        _sentiment = pipeline("sentiment-analysis")
    return _sentiment


def analyze_sentiment(comment: str) -> Dict[str, Any]:
    """Analyze sentiment, tone, and sarcasm in a comment."""
    try:
        res = get_sentiment()(comment)[0]
        lbl, scr = res["label"], res["score"]

        # Sentiment mapping
        sentiment = "Positive" if lbl == "POSITIVE" else "Negative"

        # Tone mapping
        tone = "Excited" if (sentiment == "Positive" and scr > 0.9) else \
               "Angry" if (sentiment == "Negative" and scr > 0.9) else "Neutral"

        # Sarcasm detection
        sarcasm = "Sarcastic" if any(p.search(comment) for p in SARCASM_PATTERNS) else "Not Sarcastic"

        return {
            "sentiment": sentiment,
            "tone": tone,
            "sarcasm": sarcasm,
            "score": {"label": lbl, "score": round(scr, 2)},
        }

    except Exception as e:
        return {"error": str(e)}


def display_results(comment: str, result: Dict[str, Any]) -> None:
    """Pretty print results."""
    print("\n" + "-" * 50)
    print("Comment:\n" + textwrap.fill(comment, width=50) + "\n")

    for k, v in result.items():
        if isinstance(v, dict):
            print("Score Breakdown:")
            for sub_k, sub_v in v.items():
                print(f"  {sub_k.capitalize()}: {sub_v}")
        else:
            print(f"{k.capitalize()}: {v}")
    print("-" * 50 + "\n")


def main() -> None:
    """Interactive CLI for sentiment analysis."""
    print("Welcome to the Sentiment Analysis Tool!")
    while True:
        c = input("Enter a comment (or type 'exit' to quit): ").strip()
        if not c:
            print("⚠️ Please enter a valid comment.")
            continue
        if c.lower() == "exit":
            print("Exiting...")
            break

        res = analyze_sentiment(c)
        display_results(c, res)


if __name__ == "__main__":
    main()
