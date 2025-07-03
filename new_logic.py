import re
from transformers import pipeline
from typing import Dict, Union

# Constants
MAX_LEN = 512
SARCASM_RE = re.compile(r"\b(totally|yeah right|not sure|obviously|sure thing)\b", re.IGNORECASE)

def load_model():
    """Load the sentiment analysis model."""
    try:
        return pipeline("sentiment-analysis", truncation=True, max_length=MAX_LEN)
    except Exception as e:
        raise RuntimeError(f"Model loading failed: {e}")

def is_sarcastic(text: str) -> bool:
    """Check for sarcasm using regex."""
    return bool(SARCASM_RE.search(text))

def get_tone(label: str, score: float) -> str:
    """Determine emotional tone from sentiment and confidence score."""
    if label == "POSITIVE":
        return "Excited" if score > 0.9 else "Happy"
    if label == "NEGATIVE":
        return "Angry" if score > 0.9 else "Upset"
    return "Neutral"

def analyze(text: str, model) -> Dict[str, Union[str, float]]:
    """Perform sentiment and sarcasm analysis."""
    try:
        res = model(text)[0]
        label, score = res["label"], round(res["score"], 2)
        return {
            "Comment": text,
            "Sentiment": label,
            "Tone": get_tone(label, score),
            "Sarcasm": "Sarcastic" if is_sarcastic(text) else "Not Sarcastic",
            "Score": score
        }
    except Exception as e:
        raise RuntimeError(f"Analysis failed: {e}")

def main():
    """Interactive CLI for sentiment analysis."""
    print("\n🧠 Sentiment Analyzer (type 'exit' to quit)\n")
    model = load_model()

    while True:
        text = input("Enter a comment: ").strip()
        if text.lower() == "exit":
            print("👋 Goodbye!")
            break
        if not text:
            print("⚠️ Please enter a non-empty comment.")
            continue

        try:
            result = analyze(text, model)
            print("\n📊 Analysis Result:")
            for k, v in result.items():
                print(f"{k}: {v}")
        except Exception as e:
            print(f"⚠️ Error: {e}")

        if input("\nAnalyze another? (Y/N): ").strip().lower() != 'y':
            print("👋 Goodbye!")
            break

if __name__ == "__main__":
    main()
