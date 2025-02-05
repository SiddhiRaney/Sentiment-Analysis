import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import re

# Download dependencies silently
nltk.download('vader_lexicon', quiet=True)

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Optimized sarcasm pattern with word boundaries and improved regex grouping
SARCASM_PATTERN = re.compile(
    r'\b(?:not sure|oh great|yeah right|totally|just perfect|as if|sure thing|love that|so fun|what a joy|'
    r'fantastic|just wonderful|couldn\'t be better|amazing work|brilliant idea|so helpful)\b',
    re.IGNORECASE
)

def analyze_sentiment(comment: str):
    """Analyzes the sentiment of a comment and detects possible sarcasm."""
    sentiment_scores = sia.polarity_scores(comment)
    compound_score = sentiment_scores['compound']
    
    # Classify sentiment using concise ternary conditions
    sentiment = 'Positive' if compound_score >= 0.05 else 'Negative' if compound_score <= -0.05 else 'Neutral'
    
    # Detect sarcasm using compiled regex
    if SARCASM_PATTERN.search(comment):
        return 'Sarcastic', True, compound_score
    
    return sentiment, False, compound_score

def main():
    """Runs the sentiment analysis loop for user input."""
    print("\nSentiment & Sarcasm Analyzer\n" + "=" * 30)
    
    while (comment := input("\nEnter a comment (or type 'exit' to quit): ").strip().lower()) != 'exit':
        if not comment:
            print("Empty input detected. Please enter a valid comment.")
            continue
        
        sentiment, sarcasm, score = analyze_sentiment(comment)
        print(f"\n{'-' * 34}\nComment: {comment}\nSentiment: {sentiment}\nSarcasm Detection: {'Yes' if sarcasm else 'No'}\nSentiment Score: {score:.2f}\n{'-' * 34}")
    
    print("Exiting the program. Goodbye!")

if __name__ == "__main__":
    main()
