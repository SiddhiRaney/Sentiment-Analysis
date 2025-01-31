import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import re

# Download vader_lexicon if not already done
nltk.download('vader_lexicon')

# Initialize the VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(comment):
    """Analyzes the sentiment of a comment and detects possible sarcasm."""
    sentiment_scores = sia.polarity_scores(comment)
    compound_score = sentiment_scores['compound']

    # Classify sentiment
    if compound_score >= 0.05:
        sentiment = 'Positive'
    elif compound_score <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    # Improved sarcasm detection using regex
    sarcasm_patterns = r'\b(?:not sure|oh great|yeah right|totally|just perfect|as if)\b'
    sarcasm_detected = 'Sarcastic' if re.search(sarcasm_patterns, comment, re.IGNORECASE) else 'Not Sarcastic'

    return sentiment, sarcasm_detected, compound_score

def main():
    """Runs the sentiment analysis loop for user input."""
    while True:
        comment = input("\nEnter a comment: ").strip()
        
        if not comment:
            print("Empty input detected. Please enter a valid comment.")
            continue

        sentiment, sarcasm, score = analyze_sentiment(comment)
        
        # Display results
        print(f"\nComment: {comment}")
        print(f"Sentiment: {sentiment}")
        print(f"Sarcasm Detection: {sarcasm}")
        print(f"Sentiment Score: {score:.2f}\n")

        # Continue or exit
        choice = input("Do you want to analyze another comment? (Y/N): ").strip().lower()
        if choice != 'y':
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()
