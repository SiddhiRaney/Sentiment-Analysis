import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download and initialize VADER
try:
    nltk.download('vader_lexicon', quiet=True)
    sia = SentimentIntensityAnalyzer()
except Exception as e:
    print(f"Error initializing Sentiment Analyzer: {e}")
    exit(1)

def analyze_sentiment(text):
    """Analyze the sentiment, tone, and sarcasm of a given text."""
    try:
        scores = sia.polarity_scores(text)
        compound_score = scores['compound']

        # Determine sentiment
        sentiment = (
            'Positive' if compound_score >= 0.05 else
            'Negative' if compound_score <= -0.05 else
            'Neutral'
        )

        # Determine tone
        pos, neg, neu = scores['pos'], scores['neg'], scores['neu']
        tone = (
            'Excited' if pos > 0.7 else
            'Angry' if neg > 0.7 else
            'Calm' if neu > 0.9 else
            'Happy' if pos > neg else
            'Sad' if neg > pos else
            'Mixed'
        )

        # Detect sarcasm
        sarcasm_keywords = {'not', 'sure', 'yeah right', 'totally'}
        sarcasm = 'Sarcastic' if any(word in text.lower() for word in sarcasm_keywords) else 'Not Sarcastic'

        return sentiment, tone, sarcasm, round(compound_score, 2)
    except Exception as e:
        raise RuntimeError(f"Error analyzing sentiment: {e}")

def main():
    """Interactive sentiment analysis tool."""
    print("\n📊 Sentiment Analysis Tool\nEnter comments for analysis (type 'exit' to quit).\n")

    while True:
        try:
            comment = input("Enter a comment: ").strip()
            if comment.lower() == 'exit':
                print("Exiting... Thank you for using the tool!")
                break

            if not comment:
                print("⚠️ Please enter a valid comment!")
                continue

            sentiment, tone, sarcasm, compound_score = analyze_sentiment(comment)
            print(f"\n📝 Comment: {comment}\n✅ Sentiment: {sentiment}\n🎭 Tone: {tone}\n😎 Sarcasm: {sarcasm}\n📈 Score: {compound_score}\n")

        except KeyboardInterrupt:
            print("\nInterrupted. Exiting the program.")
            break
        except RuntimeError as e:
            print(f"⚠️ Analysis Error: {e}")
        except Exception as e:
            print(f"❗ Unexpected Error: {e}")

        if input("Analyze another? (Y/N): ").strip().lower() != 'y':
            print("👋 Goodbye!")
            break

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"🚨 Critical Error: {e}")
