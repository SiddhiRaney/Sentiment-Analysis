import re
from transformers import pipeline

# Constants
MAX_TEXT_LENGTH = 512
SARCASM_KEYWORDS = {"totally", "yeah right", "not sure", "obviously", "sure thing"}

def load_sentiment_model():
    """Load and return the sentiment analysis model."""
    try:
        return pipeline("sentiment-analysis", truncation=True, max_length=MAX_TEXT_LENGTH)
    except Exception as e:
        raise RuntimeError(f"Failed to load sentiment model: {e}")

def detect_sarcasm(text):
    """Detect sarcasm using keyword matching."""
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in SARCASM_KEYWORDS)

def determine_tone(label, score):
    """Determine the tone based on sentiment label and score."""
    if label == "POSITIVE":
        return "Excited" if score > 0.9 else "Happy"
    elif label == "NEGATIVE":
        return "Angry" if score > 0.9 else "Upset"
    return "Neutral"

def analyze_sentiment(text, model):
    """Analyze sentiment and detect sarcasm from input text."""
    try:
        result = model(text)[0]
        label = result['label']
        score = round(result['score'], 2)
        tone = determine_tone(label, score)
        sarcasm = "Sarcastic" if detect_sarcasm(text) else "Not Sarcastic"
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
    """Interactive CLI for sentiment analysis."""
    print("\n🧠 AI Sentiment Analysis Tool (type 'exit' to quit)\n")
    model = load_sentiment_model()

    while True:
        text = input("Enter a comment: ").strip()
        if text.lower() == "exit":
            print("Exiting... Goodbye!")
            break
        if not text:
            print("Please enter a valid comment.")
            continue

        try:
            result = analyze_sentiment(text, model)
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
