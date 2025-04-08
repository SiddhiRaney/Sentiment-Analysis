import torch
from transformers import pipeline

# Constants
MAX_TEXT_LENGTH = 512
SARCASM_KEYWORDS = {"totally", "yeah right", "not sure", "obviously", "sure thing"}

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

        tone = {
            "POSITIVE": "Excited" if score > 0.9 else "Happy",
            "NEGATIVE": "Angry" if score > 0.9 else "Upset"
        }.get(label, "Neutral")

        sarcasm = "Sarcastic" if any(kw in text for kw in SARCASM_KEYWORDS) else "Not Sarcastic"

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
    print("\nAI Sentiment Analysis Tool (Type 'exit' to quit)\n")
    model = load_sentiment_model()

    while True:
        raw_text = input("Enter a comment: ").strip()
        text = raw_text.lower()

        if text == "exit":
            print("Exiting... Goodbye!")
            break
        if not text:
            print("Invalid input. Please enter a valid comment.")
            continue

        try:
            result = analyze_sentiment(text, model)
            print("\nAnalysis Result:")
            for k, v in result.items():
                print(f"{k}: {v}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

        again = input("Analyze another? (Y/N): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
