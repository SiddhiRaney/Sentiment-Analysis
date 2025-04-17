import re
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
        compound = scores['compound']
        pos, neg, neu = scores['pos'], scores['neg'], scores['neu']

        # Sentiment classification
        if compound >= 0.05:
            sentiment = 'Positive'
        elif compound <= -0.05:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'

        # Tone classification
        if pos >= 0.7:
            tone = 'Excited'
        elif neg >= 0.7:
            tone = 'Angry'
        elif neu >= 0.9:
            tone = 'Calm'
        elif pos > neg:
            tone = 'Happy'
        elif neg > pos:
            tone = 'Sad'
        else:
            tone = 'Mixed'

        # Sarcasm detection using pattern-based keyword matching
        sarcasm_patterns = [
            r"\bnot\b.*\bgood\b",
            r"\bsure\b",
            r"yeah right",
            r"totally\b.*(awesome|great)",
        ]
        sarcasm = 'Sarcastic' if any(re.search(pattern, text.lower()) for pattern in sarcasm_patterns) else 'Not Sarcastic'

        return sentiment, tone, sarcasm, round(compound, 2)
    except Exception as e:
        raise RuntimeError(f"Error analyzing sentiment: {e}")

def main():
    """Interactive sentiment analysis tool."""
    print("\nSentiment Analysis Tool")
    print("Enter comments for analysis (type 'exit' to quit).\n")

    while True:
        try:
            comment = input("Enter a comment: ").strip()
            if comment.lower() == 'exit':
                print("Exiting... Thank you for using the tool.")
                break

            if not comment:
                print("Please enter a valid comment.")
                continue

            sentiment, tone, sarcasm, compound_score = analyze_sentiment(comment)
            print(f"\nComment: {comment}")
            print(f"Sentiment: {sentiment}")
            print(f"Tone: {tone}")
            print(f"Sarcasm: {sarcasm}")
            print(f"Score: {compound_score}\n")

        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting.")
            break
        except RuntimeError as e:
            print(f"Analysis Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

        again = input("Analyze another? (Y/N): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Critical Error: {e}")
