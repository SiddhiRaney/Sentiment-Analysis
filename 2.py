import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import re

# Download vader_lexicon if not already done
nltk.download('vader_lexicon', quiet=True)

# Initialize the VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Precompiled regex for sarcasm detection
SARCASM_PATTERN = re.compile(r'\b(?:not sure|oh great|yeah right|totally|just perfect|as if|sure thing|love that|so fun)\b', re.IGNORECASE)

def analyze_sentiment(comment):
    """Analyzes the sentiment of a comment and detects possible sarcasm."""
    sentiment_scores = sia.polarity_scores(comment)
    compound_score = sentiment_scores['compound']

    # Classify sentiment
    sentiment = 'Positive' if compound_score >= 0.05 else 'Negative' if compound_score <= -0.05 else 'Neutral'
    sarcasm_detected = 'Sarcastic' if SARCASM_PATTERN.search(comment) else 'Not Sarcastic'

    return sentiment, sarcasm_detected, compound_score

def main():
    """Runs the sentiment analysis loop for user input."""
    while True:
        comment = input("\nEnter a comment (or type 'exit' to quit): ").strip()
        
        if comment.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        elif not comment:
            print("Empty input detected. Please enter a valid comment.")
            continue

        sentiment, sarcasm, score = analyze_sentiment(comment)
        
        # Display results
        print(f"\nComment: {comment}\nSentiment: {sentiment}\nSarcasm Detection: {sarcasm}\nSentiment Score: {score:.2f}\n")

if __name__ == "__main__":
    main()
