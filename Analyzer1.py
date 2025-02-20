import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download and initialize VADER
try:
    nltk.download('vader_lexicon')
    sia = SentimentIntensityAnalyzer()
except Exception as e:
    print(f"Error initializing Sentiment Analyzer: {e}")
    exit(1)

def analyze_sentiment(text):
    """Analyze the sentiment, tone, and sarcasm of a given text."""
    try:
        scores = sia.polarity_scores(text)
        compound_score = scores.get('compound', 0.0)

        sentiment = (
            'Positive' if compound_score >= 0.05 else
            'Negative' if compound_score <= -0.05 else
            'Neutral'
        )

        tone = (
            'Excited' if scores.get('pos', 0) > 0.7 else
            'Angry' if scores.get('neg', 0) > 0.7 else
            'Calm' if scores.get('neu', 0) > 0.9 else
            'Happy' if scores.get('pos', 0) > scores.get('neg', 0) else
            'Sad' if scores.get('neg', 0) > scores.get('pos', 0) else
            'Mixed'
        )

        sarcasm_keywords = {'not', 'sure', 'yeah right', 'totally'}
        sarcasm = 'Sarcastic' if any(word in text.lower() for word in sarcasm_keywords) else 'Not Sarcastic'

        return sentiment, tone, sarcasm, compound_score
    except Exception as e:
        raise RuntimeError(f"Error analyzing sentiment: {e}")

def main():
    """Interactive sentiment analysis program with exception handling."""
    print("\nSentiment Analysis Tool\nEnter comments for analysis (type 'exit' to quit).\n")

    while True:
        try:
            comment = input("Enter a comment: ").strip()
            if comment.lower() == 'exit':
                print("Exiting... Thank you for using the tool!")
                break

            if not comment:
                print("Please enter a valid comment!")
                continue

            sentiment, tone, sarcasm, compound_score = analyze_sentiment(comment)
            print(f"\nComment: {comment}\nSentiment: {sentiment}\nTone: {tone}\nSarcasm: {sarcasm}\nScore: {compound_score:.2f}\n")

        except RuntimeError as e:
            print(f"Analysis Error: {e}")
        except KeyboardInterrupt:
            print("\nInterrupted. Exiting the program.")
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
