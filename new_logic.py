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
        results = model([text])
        label, score = results[0]['label'], round(results[0]['score'], 2)

        if label == "POSITIVE":
            tone = "Excited" if score > 0.9 else "Happy"
        elif label == "NEGATIVE":
            tone = "Angry" if score > 0.9 else "Upset"
        else:
            tone = "Neutral"

        sarcasm_detected = any(keyword in text.lower() for keyword in sarcasm_keywords)
        sarcasm = "Sarcastic" if sarcasm_detected else "Not Sarcastic"

        return {"Comment": text, "Sentiment": label, "Tone": tone, "Sarcasm": sarcasm, "Score": score}
    except Exception as e:
        raise RuntimeError(f"Error analyzing sentiment: {e}")

def main():
    """Optimized interactive sentiment analysis tool."""
    print("\nAI Sentiment Analysis Tool (Type 'exit' to quit)\n")
    model = load_sentiment_model()
    sarcasm_keywords = {"totally", "yeah right", "not sure", "obviously", "sure thing"}

    while True:
        text = input("Enter a comment: ").strip()
        
        if not text:
            print("Invalid input. Please enter a valid comment.")
            continue
        if text.lower() == 'exit':
            print("Exiting... Goodbye!")
            break

        try:
            result = analyze_sentiment(text, model, sarcasm_keywords)
            print("\nAnalysis Result:")
            for key, value in result.items():
                print(f"{key}: {value}")
            print()

            next_action = input("Analyze another? (Y/N): ").strip().lower()
            if next_action != 'y':
                print("Goodbye!")
                break
        except Exception as e:
            print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    main()
