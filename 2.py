import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import re

# Download vader_lexicon if not already done
nltk.download('vader_lexicon', quiet=True)

# Initialize the VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Expanded sarcasm detection with more phrases and improved regex pattern
SARCASM_PATTERN = re.compile(r'\b(?:not sure|oh great|yeah right|totally|just perfect|as if|sure thing|love that|so fun|what a joy|fantastic|just wonderful|couldn\'t be better|amazing work|brilliant idea|so helpful)\b', re.IGNORECASE)

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

    # Detect sarcasm
    sarcasm_detected = bool(SARCASM_PATTERN.search(comment))
    
    # If sarcasm is detected and sentiment is positive, adjust classification
    if sarcasm_detected and sentiment == 'Positive':
        sentiment = 'Sarcastic'
    
    return sentiment, sarcasm_detected, compound_score

def main():
    """Runs the sentiment analysis loop for user input."""
    print("\nSentiment & Sarcasm Analyzer\n" + "=" * 30)
    
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
        print("\n----------------------------------")
        print(f"Comment: {comment}")
        print(f"Sentiment: {sentiment}")
        print(f"Sarcasm Detection: {'Yes' if sarcasm else 'No'}")
        print(f"Sentiment Score: {score:.2f}")
        print("----------------------------------")

if __name__ == "__main__":
    main()
