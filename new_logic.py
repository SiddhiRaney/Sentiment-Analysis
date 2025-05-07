import re
from transformers import pipeline
from typing import Dict

# Constants
MAX_TEXT_LENGTH = 512
SARCASM_PATTERNS = re.compile(r"\b(totally|yeah right|not sure|obviously|sure thing)\b", re.IGNORECASE)

def load_sentiment_model():
    """Load and return the sentiment analysis model."""
    try:
        return pipeline("sentiment-analysis", truncation=True, max_length=MAX_TEXT_LENGTH)
    except Exception as e:
        raise RuntimeError(f"Failed to load sentiment model: {e}")

def detect_sarcasm(text: str) -> bool:
    """Detect sarcasm using regex pattern matching."""
    return bool(SARCASM_PATTERNS.search(text))

def determine_tone(label: str, score: float) -> str:
    """Map sentiment and score to a specific tone."""
    if label == "POSITIVE":
        return "Excited" if score > 0.9 else "Happy"
    elif label == "NEGATIVE":
        return "Angry" if score > 0.9 else "Upset"
    return "Neutral"

def analyze_sentiment(text: str, model) -> Dict[str, str]:
    """Run sentiment and sarcasm analysis on the given text."""
    try:
        result = model(text)[0]
        label = result['label']
        score = round(result['score'], 2)
        return {
            "Comment": text,
            "Sentiment": label,
            "Tone": determine_tone(label, score),
            "Sarcasm": "Sarcastic" if detect_sarcasm(text) else "Not Sarcastic",
            "Score": score
        }
    except Exception as e:
        raise RuntimeError(f"Error analyzing sentiment: {e}")

def main():
    """Run the interactive CLI."""
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
            for key, value in result.items():
                print(f"{key}: {value}")
        except Exception as err:
            print(f"⚠️ Error: {err}")

        if input("\nAnalyze another? (Y/N): ").strip().lower() != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
