import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import re
import sys

# Download VADER lexicon silently if missing
nltk.download("vader_lexicon", quiet=True)

try:
    sia = SentimentIntensityAnalyzer()
except Exception as e:
    sys.exit(f"Error initializing sentiment analyzer: {e}")

# Precompiled regex for sarcastic phrases
SARCASM_PATTERN = re.compile(
    r'\b(?:not sure|oh great|yeah right|totally|just perfect|as if|sure thing|love that|so fun|what a joy|'
    r'fantastic|just wonderful|couldn\'t be better|amazing work|brilliant idea|so helpful)\b',
    re.IGNORECASE
)

def analyze_sentiment(comment: str):
    """Return sentiment, sarcasm flag, and compound score for a comment."""
    try:
        scores = sia.polarity_scores(comment)
        comp = scores["compound"]

        sentiment = (
            "Positive" if comp >= 0.05
            else "Negative" if comp <= -0.05
            else "Neutral"
        )
        sarcasm = bool(SARCASM_PATTERN.search(comment))
        return sentiment, sarcasm, comp

    except Exception:
        return "Unknown", False, 0.0

def main():
    print("\nSentiment & Sarcasm Analyzer\n" + "=" * 30)

    while True:
        try:
            comment = input("\nEnter a comment (or type 'exit' to quit): ").strip()
            if not comment:
                print("⚠️ Please enter a valid comment.")
                continue
            if comment.lower() == "exit":
                break

            sentiment, sarcasm, score = analyze_sentiment(comment)

            print("\n" + "-" * 34)
            print(f"Comment         : {comment}")
            print(f"Sentiment       : {sentiment}")
            print(f"Sarcasm Detected: {'Yes' if sarcasm else 'No'}")
            print(f"Sentiment Score : {score:.2f}")
            print("-" * 34)

        except KeyboardInterrupt:
            print("\nInterrupted. Exiting...")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")

    print("Goodbye!")

if __name__ == "__main__":
    main()
