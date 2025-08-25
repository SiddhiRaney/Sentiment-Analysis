import re
from transformers import pipeline
from typing import Dict, Union

# Constants
MAX_LEN = 512
SARCASM_RE = re.compile(r"\b(totally|yeah right|not sure|obviously|sure thing)\b", re.IGNORECASE)

def load_model():
    """Load the sentiment analysis model."""
    return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def is_sarcastic(text: str) -> bool:
    """Check for sarcasm using regex."""
    return bool(SARCASM_RE.search(text))

def get_tone(label: str, score: float) -> str:
    """Determine emotional tone from sentiment and confidence score."""
    tones = {
        "POSITIVE": ("Happy", "Excited"),
        "NEGATIVE": ("Upset", "Angry"),
        "NEUTRAL": ("Neutral", "Neutral")
    }
    if label in tones:
        return tones[label][1] if score > 0.9 else tones[label][0]
    return "Neutral"

def analyze(text: str, model) -> Dict[str, Union[str, float]]:
    """Perform sentiment and sarcasm analysis."""
    res = model(text, truncation=True, max_length=MAX_LEN)[0]
    label, score = res["label"].upper(), round(res["score"], 2)
    
    return {
        "Comment": text,
        "Sentiment": label,
        "Tone": get_tone(label, score),
        "Sarcasm": "Sarcastic" if is_sarcastic(text) else "Not Sarcastic",
        "Score": score
    }

def main():
    """Interactive CLI for sentiment analysis."""
    print("\n🧠 Sentiment Analyzer (type 'exit' to quit)\n")
    try:
        model = load_model()
    except Exception as e:
        print(f"⚠️ Model loading failed: {e}")
        return

    while True:
        text = input("Enter a comment: ").strip()
        if text.lower() == "exit":
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
            break

    print("👋 Goodbye!")

if __name__ == "__main__":
    main()
