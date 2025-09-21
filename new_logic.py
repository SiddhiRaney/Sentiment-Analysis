import re
from functools import lru_cache
from transformers import pipeline
from typing import Dict

# ---------- Constants ----------
MAX_LEN = 512
SARCASM_RE = re.compile(
    r"\b(totally|yeah right|not sure|obviously|sure thing)\b",
    re.IGNORECASE
)

TONES = {
    "POSITIVE": ("Happy", "Excited"),
    "NEGATIVE": ("Upset", "Angry"),
    "NEUTRAL": ("Neutral", "Neutral"),
}


# ---------- Model Loader ----------
@lru_cache(maxsize=1)
def load_model():
    """Load and cache the sentiment analysis model once."""
    return pipeline(
        task="sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )


# ---------- Helpers ----------
def is_sarcastic(text: str) -> bool:
    """Detect sarcasm with regex pattern matching."""
    return bool(SARCASM_RE.search(text))


def get_tone(label: str, score: float) -> str:
    """Return tone based on sentiment label and confidence score."""
    tones = TONES.get(label, ("Neutral", "Neutral"))
    return tones[1] if score > 0.9 else tones[0]


# ---------- Core Analyzer ----------
def analyze(text: str, model) -> Dict[str, str]:
    """Run sentiment + sarcasm analysis and return structured results."""
    res = model(text, truncation=True, max_length=MAX_LEN)[0]
    label = res["label"].upper()
    score = round(res["score"], 2)

    return {
        "Comment": text,
        "Sentiment": label,
        "Tone": get_tone(label, score),
        "Sarcasm": "Sarcastic" if is_sarcastic(text) else "Not Sarcastic",
        "Score": score,
    }


# ---------- CLI ----------
def main():
    """CLI for interactive sentiment analysis."""
    print("\n🧠 Sentiment Analyzer (type 'exit' anytime)\n")

    try:
        model = load_model()
    except Exception as e:
        print(f"⚠️ Could not load model: {e}")
        return

    while True:
        text = input("Enter a comment: ").strip()
        if not text:
            print("⚠️ Please enter a non-empty comment.")
            continue
        if text.lower() == "exit":
            print("👋 Goodbye!")
            break

        try:
            result = analyze(text, model)
            print("\n📊 Analysis Result:")
            for k, v in result.items():
                print(f"{k}: {v}")
        except Exception as e:
            print(f"⚠️ Error during analysis: {e}")


if __name__ == "__main__":
    main()
