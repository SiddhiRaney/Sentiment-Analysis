import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import re

# Download dependencies silently
try:
    nltk.download('vader_lexicon', quiet=True)
    sia = SentimentIntensityAnalyzer()
except Exception as e:
    print(f"Error initializing sentiment analyzer: {e}")
    exit(1)

# Optimized sarcasm pattern
SARCASM_PATTERN = re.compile(
    r'\b(?:not sure|oh great|yeah right|totally|just perfect|as if|sure thing|love that|so fun|what a joy|'
    r'fantastic|just wonderful|couldn\'t be better|amazing work|brilliant idea|so helpful)\b',
    re.IGNORECASE
)

def analyze_sentiment(comment: str):
    """Analyzes the sentiment of a comment and detects possible sarcasm."""
    try:
        sentiment_scores = sia.polarity_scores(comment)
        compound_score = sentiment_scores.get('compound', 0)
        
        sentiment = (
            'Positive' if compound_score >= 0.05 
            else 'Negative' if compound_score <= -0.05 
            else 'Neutral'
        )
        
        sarcasm = bool(SARCASM_PATTERN.search(comment))
        
        return sentiment, sarcasm, compound_score
    except Exception as e:
        print(f"Error analyzing sentiment: {e}")
        return 'Unknown', False, 0.0

def main():
    """Runs the sentiment analysis loop for user input."""
    print("\nSentiment & Sarcasm Analyzer\n" + "=" * 30)
    
    while True:
        try:
            comment = input("\nEnter a comment (or type 'exit' to quit): ").strip()
            if comment.lower() == 'exit':
                break
            if not comment:
                print("Empty input detected. Please enter a valid comment.")
                continue
            
            sentiment, sarcasm, score = analyze_sentiment(comment)
            print(f"\n{'-' * 34}\nComment: {comment}\nSentiment: {sentiment}\n"
                  f"Sarcasm Detection: {'Yes' if sarcasm else 'No'}\n"
                  f"Sentiment Score: {score:.2f}\n{'-' * 34}")
        except KeyboardInterrupt:
            print("\nUser interrupted. Exiting the program.")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
    
    print("Exiting the program. Goodbye!")

if __name__ == "__main__":
    main()
