import torch
from transformers import pipeline

def load_sentiment_model():
    """Load a transformer-based sentiment analysis model."""
    try:
        return pipeline("sentiment-analysis")
    except Exception as e:
        raise RuntimeError(f"Error loading sentiment model: {e}")

def load_sarcasm_model():
    """Placeholder for sarcasm detection model."""
    # In a real-world application, we would use a fine-tuned sarcasm detection model
    sarcasm_keywords = {"totally", "yeah right", "not sure", "obviously", "sure thing"}
    return sarcasm_keywords

def analyze_sentiment(text, sentiment_model, sarcasm_model):
    """Analyze sentiment and sarcasm using AI models."""
    try:
        sentiment_result = sentiment_model(text)[0]
        sentiment_label = sentiment_result['label']
        sentiment_score = sentiment_result['score']
        
        # Determine tone
        tone = "Calm"
        if sentiment_label == "POSITIVE" and sentiment_score > 0.9:
            tone = "Excited"
        elif sentiment_label == "NEGATIVE" and sentiment_score > 0.9:
            tone = "Angry"
        elif 0.4 < sentiment_score < 0.6:
            tone = "Neutral"
        
        # Sarcasm detection
        sarcasm = "Sarcastic" if any(word in text.lower() for word in sarcasm_model) else "Not Sarcastic"
        
        return sentiment_label, tone, sarcasm, sentiment_score
    except Exception as e:
        raise RuntimeError(f"Error analyzing sentiment: {e}")

def main():
    """Interactive AI-based sentiment analysis tool."""
    print("\nAI Sentiment Analysis Tool\nType 'exit' to quit.\n")
    
    sentiment_model = load_sentiment_model()
    sarcasm_model = load_sarcasm_model()
    
    while True:
        try:
            comment = input("Enter a comment: ").strip()
            if comment.lower() == 'exit':
                print("Exiting... Goodbye!")
                break

            if not comment:
                print("Please enter a valid comment!")
                continue
            
            sentiment, tone, sarcasm, score = analyze_sentiment(comment, sentiment_model, sarcasm_model)
            print(f"\nComment: {comment}\nSentiment: {sentiment}\nTone: {tone}\nSarcasm: {sarcasm}\nScore: {score:.2f}\n")

        except RuntimeError as e:
            print(f"Analysis Error: {e}")
        except KeyboardInterrupt:
            print("\nInterrupted. Exiting...")
            break
        except Exception as e:
            print(f"Unexpected Error: {e}")

        retry = input("Analyze another? (Y/N): ").strip().lower()
        if retry != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Critical Error: {e}")
