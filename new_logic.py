import torch
from transformers import pipeline

def load_sentiment_model():
    """Load a transformer-based sentiment analysis model."""
    try:
        return pipeline("sentiment-analysis")
    except Exception as e:
        raise RuntimeError(f"Error loading sentiment model: {e}")

def analyze_sentiment(text, model, sarcasm_keywords):
    """Analyze sentiment and detect sarcasm efficiently."""
    try:
        result = model(text, truncation=True, max_length=512)[0]
        label, score = result['label'], round(result['score'], 2)

        tone_map = {
            "POSITIVE": "Excited" if score > 0.9 else "Happy",
            "NEGATIVE": "Angry" if score > 0.9 else "Upset",
            "NEUTRAL": "Neutral"
        }
        tone = tone_map.get(label, "Neutral")

        sarcasm = "Sarcastic" if any(keyword in text.lower() for keyword in sarcasm_keywords) else "Not Sarcastic"

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
    """Optimized interactive sentiment analysis tool."""
    print("\nAI Sentiment Analysis Tool (Type 'exit' to quit)\n")
    model = load_sentiment_model()
    sarcasm_keywords = {"totally", "yeah right", "not sure", "obviously", "sure thing"}

    while True:
        text = input("Enter a comment: ").strip().lower()

        if text == 'exit':
            print("Exiting... Goodbye!")
            break
        if not text:
            print("Invalid input. Please enter a valid comment.")
            continue

        try:
            result = analyze_sentiment(text, model, sarcasm_keywords)
            print("\nAnalysis Result:")
            print("\n".join(f"{key}: {value}" for key, value in result.items()))
        except Exception as e:
            print(f"Unexpected Error: {e}")

        if input("Analyze another? (Y/N): ").strip().lower() != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
