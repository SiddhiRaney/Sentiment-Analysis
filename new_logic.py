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
        result = model(text)[0]
        label, score = result['label'], round(result['score'], 2)
        
        tone = (
            "Excited" if label == "POSITIVE" and score > 0.9 else
            "Happy" if label == "POSITIVE" else
            "Angry" if label == "NEGATIVE" and score > 0.9 else
            "Upset" if label == "NEGATIVE" else
            "Neutral"
        )
        
        sarcasm = "Sarcastic" if any(word in text.lower() for word in sarcasm_keywords) else "Not Sarcastic"
        
        return {"Comment": text, "Sentiment": label, "Tone": tone, "Sarcasm": sarcasm, "Score": score}
    except Exception as e:
        raise RuntimeError(f"Error analyzing sentiment: {e}")

def main():
    """Optimized interactive sentiment analysis tool."""
    print("\nAI Sentiment Analysis Tool (Type 'exit' to quit)\n")
    model = load_sentiment_model()
    sarcasm_keywords = {"totally", "yeah right", "not sure", "obviously", "sure thing"}
    
    while True:
        try:
            text = input("Enter a comment: ").strip()
            if text.lower() == 'exit':
                print("Exiting... Goodbye!")
                break
            if not text:
                print("Invalid input. Please enter a valid comment.")
                continue
            
            result = analyze_sentiment(text, model, sarcasm_keywords)
            print("\nAnalysis Result:")
            for key, value in result.items():
                print(f"{key}: {value}")
            print()
            
            if input("Analyze another? (Y/N): ").strip().lower() != 'y':
                print("Goodbye!")
                break
        except (KeyboardInterrupt, EOFError):
            print("\nInterrupted. Exiting...")
            break
        except Exception as e:
            print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Critical Error: {e}")
