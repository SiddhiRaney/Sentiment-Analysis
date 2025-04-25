import torch
import re
from transformers import pipeline

# Constants
MAX_TEXT_LENGTH = 512
SARCASM_KEYWORDS = {"totally", "yeah right", "not sure", "obviously", "sure thing"}
SARCASM_PATTERN = re.compile(r"\b(" + "|".join(re.escape(word) for word in SARCASM_KEYWORDS) + r")\b", re.IGNORECASE)

def load_sentiment_model():
    """Load transformer-based sentiment analysis model."""
    try:
        return pipeline("sentiment-analysis")
    except Exception as e:
        raise RuntimeError(f"Error loading sentiment model: {e}")

def analyze_sentiment(text, model):
    """Analyze sentiment and detect sarcasm."""
    try:
        result = model(text, truncation=True, max_length=MAX_TEXT_LENGTH)[0]
        label, score = result['label'], round(result['score'], 2)

        tone = "Neutral"
        if label == "POSITIVE":
            tone = "Excited" if score > 0.9 else "Happy"
        elif label == "NEGATIVE":
            tone = "Angry" if score > 0.9 else "Upset"

        sarcasm = "Sarcastic" if SARCASM_PATTERN.search(text) else "Not Sarcastic"

        return {
            "Comment": text,
            "Sentiment": label,
            "Tone": tone,
            "Sarcasm": sarcasm,
            "Score": score
        }
    except Exception as e:
        raise RuntimeError(f"Error analyzing sentiment: {e}")

def main():
    """Interactive sentiment analysis console."""
    print("\n🧠 AI Sentiment Analysis Tool (type 'exit' to quit)\n")
    model = load_sentiment_model()

    while True:
        raw_text = input("Enter a comment: ").strip()
        if not raw_text:
            print("Invalid input. Please enter a valid comment.")
            continue
        if raw_text.lower() == "exit":
            print("Exiting... Goodbye!")
            break

        try:
            result = analyze_sentiment(raw_text, model)
            print("\n📊 Analysis Result:")
            for k, v in result.items():
                print(f"{k}: {v}")
        except Exception as e:
            print(f"⚠️ Error: {e}")

        again = input("\nAnalyze another? (Y/N): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
