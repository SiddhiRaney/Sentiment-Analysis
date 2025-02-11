import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download and initialize VADER
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    """Analyze the sentiment, tone, and sarcasm of a given text."""
    scores = sia.polarity_scores(text)
    compound_score = scores['compound']

    sentiment = (
        'Positive' if compound_score >= 0.05 else
        'Negative' if compound_score <= -0.05 else
        'Neutral'
    )

    tone = (
        'Excited' if scores['pos'] > 0.7 else
        'Angry' if scores['neg'] > 0.7 else
        'Calm' if scores['neu'] > 0.9 else
        'Happy' if scores['pos'] > scores['neg'] else
        'Sad' if scores['neg'] > scores['pos'] else
        'Mixed'
    )

    sarcasm = 'Sarcastic' if any(word in text.lower() for word in {'not', 'sure', 'yeah right', 'totally'}) else 'Not Sarcastic'

    return sentiment, tone, sarcasm, compound_score

def main():
    """Interactive sentiment analysis program."""
    print("\nSentiment Analysis Tool\nEnter comments for analysis (type 'exit' to quit).\n")

    while True:
        comment = input("Enter a comment: ").strip()
        if comment.lower() == 'exit':
            print("Exiting... Thank you for using the tool!")
            break

        if not comment:
            print("Please enter a valid comment!")
            continue

        try:
            sentiment, tone, sarcasm, compound_score = analyze_sentiment(comment)
            print(f"\nComment: {comment}\nSentiment: {sentiment}\nTone: {tone}\nSarcasm: {sarcasm}\nScore: {compound_score:.2f}\n")
        except Exception as e:
            print(f"Error: {e}")

        if input("Analyze another? (Y/N): ").strip().lower() != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
