import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import re

# Download the VADER lexicon silently; only download if necessary
try:
    nltk.download('vader_lexicon', quiet=True)
    sia = SentimentIntensityAnalyzer()
except Exception as e:
    print(f"Error initializing sentiment analyzer: {e}")
    exit(1)

# Precompiled regex pattern to detect commonly sarcastic phrases
# These phrases are usually positive in tone but often used sarcastically depending on context
SARCASM_PATTERN = re.compile(
    r'\b(?:not sure|oh great|yeah right|totally|just perfect|as if|sure thing|love that|so fun|what a joy|'
    r'fantastic|just wonderful|couldn\'t be better|amazing work|brilliant idea|so helpful)\b',
    re.IGNORECASE
)

def analyze_sentiment(comment: str):
    """Analyze sentiment and detect sarcasm in the given comment."""
    try:
        # Get polarity scores from VADER (compound, pos, neu, neg)
        sentiment_scores = sia.polarity_scores(comment)
        compound_score = sentiment_scores.get('compound', 0)

        # Classify sentiment based on compound score threshold
        # These thresholds are based on VADER's standard practice
        sentiment = (
            'Positive' if compound_score >= 0.05 
            else 'Negative' if compound_score <= -0.05 
            else 'Neutral'
        )

        # Check for presence of any sarcastic phrases using regex
        sarcasm = bool(SARCASM_PATTERN.search(comment))

        return sentiment, sarcasm, compound_score
    except Exception as e:
        print(f"Error analyzing sentiment: {e}")
        return 'Unknown', False, 0.0

def main():
    """Interactive loop to analyze user input for sentiment and sarcasm."""
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

            # Cleanly formatted result output
            print(f"\n{'-' * 34}")
            print(f"Comment         : {comment}")
            print(f"Sentiment       : {sentiment}")
            print(f"Sarcasm Detected: {'Yes' if sarcasm else 'No'}")
            print(f"Sentiment Score : {score:.2f}")
            print(f"{'-' * 34}")
        
        except KeyboardInterrupt:
            print("\nUser interrupted. Exiting the program.")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
    
    print("Exiting the program. Goodbye!")

if __name__ == "__main__":
    main()
