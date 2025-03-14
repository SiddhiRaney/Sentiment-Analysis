import torch
from transformers import pipeline

def load_sentiment_model():
    """Load a transformer-based sentiment analysis model."""
    try:
        return pipeline("sentiment-analysis")
    except Exception as e:
        raise RuntimeError(f"Error loading sentiment model: {e}")

def load_sarcasm_keywords():
    """Return a set of common sarcasm indicators."""
    return {"totally", "yeah right", "not sure", "obviously", "sure thing"}

def analyze_sentiment(text, sentiment_model, sarcasm_keywords):
    """Analyze sentiment and detect sarcasm."""
    try:
        sentiment_result = sentiment_model(text)[0]
        sentiment_label, sentiment_score = sentiment_result['label'], sentiment_result['score']
        
        # Determine tone
        tone = "Calm"
        if sentiment_label == "POSITIVE":
            tone = "Excited" if sentiment_score > 0.9 else "Happy"
        elif sentiment_label == "NEGATIVE":
            tone = "Angry" if sentiment_score > 0.9 else "Upset"
        elif 0.4 < sentiment_score < 0.6:
            tone = "Neutral"
        
        # Sarcasm detection
        sarcasm = "Sarcastic" if any(word in text.lower() for word in sarcasm_keywords) else "Not Sarcastic"
        
        return {
            "comment": text,
            "sentiment": sentiment_label,
            "tone": tone,
            "sarcasm": sarcasm,
            "score": round(sentiment_score, 2)
        }
    except Exception as e:
        raise RuntimeError(f"Error analyzing sentiment: {e}")

def main():
    """Interactive AI-based sentiment analysis tool."""
    print("\nAI Sentiment Analysis Tool\nType 'exit' to quit.\n")
    
    sentiment_model = load_sentiment_model()
    sarcasm_keywords = load_sarcasm_keywords()
    
    while True:
        try:
            comment = input("Enter a comment: ").strip()
            if comment.lower() == 'exit':
                print("Exiting... Goodbye!")
                break

            if not comment:
                print("Please enter a valid comment!")
                continue
            
            result = analyze_sentiment(comment, sentiment_model, sarcasm_keywords)
            print("\nAnalysis Result:")
            for key, value in result.items():
                print(f"{key.capitalize()}: {value}")
            print()
        
        except RuntimeError as e:
            print(f"Analysis Error: {e}")
        except KeyboardInterrupt:
            print("\nInterrupted. Exiting...")
            break
        except Exception as e:
            print(f"Unexpected Error: {e}")

        if input("Analyze another? (Y/N): ").strip().lower() != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Critical Error: {e}")
