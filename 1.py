import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import re

# Download vader_lexicon if not already done
nltk.download('vader_lexicon', quiet=True)

# Initialize the VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Precompile sarcasm regex patterns for efficiency
SARCASM_PATTERNS = [
    re.compile(pattern, re.IGNORECASE) for pattern in [
        r'not\s+(great|good|bad|terrible|happy|sad|funny)',
        r'yeah\s+right',
        r'sure\s+thing',
        r'totally\s+(agree|disagree|true|false)',
        r'as\s+if',
        r'oh\s+really',
        r'wow\s+(amazing|incredible|fantastic)',
        r'just\s+what\s+I\s+needed',
        r'so\s+much\s+fun',
        r'love\s+that\s+for\s+me'
    ]
]

def analyze_sentiment(comment: str):
    """Analyzes sentiment and detects sarcasm in a given comment."""
    sentiment_scores = sia.polarity_scores(comment)
    compound = sentiment_scores['compound']
    
    sentiment = (
        'Positive' if compound >= 0.05 else
        'Negative' if compound <= -0.05 else
        'Neutral'
    )
    
    sarcasm = 'Sarcastic' if any(pattern.search(comment) for pattern in SARCASM_PATTERNS) else 'Not Sarcastic'
    
    return {
        "Comment": comment,
        "Sentiment": sentiment,
        "Sarcasm Detection": sarcasm,
        "Sentiment Score": round(compound, 2),
        "Scores": {
            "Positive": round(sentiment_scores['pos'], 2),
            "Neutral": round(sentiment_scores['neu'], 2),
            "Negative": round(sentiment_scores['neg'], 2)
        }
    }

def main():
    """Runs an interactive user input loop for sentiment analysis."""
    print("\nSentiment & Sarcasm Analyzer (Type 'exit' to quit)\n")
    
    while True:
        comment = input("Enter a comment: ").strip()
        if comment.lower() == 'exit':
            print("Goodbye!")
            break
        if not comment:
            print("Please enter a valid comment.")
            continue
        
        result = analyze_sentiment(comment)
        print("\n============================")
        for key, value in result.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    print(f"  - {sub_key}: {sub_value}")
            else:
                print(f"{key}: {value}")
        print("============================\n")
        
        if input("Analyze another comment? (Y/N): ").strip().lower() != 'y':
            print("Goodbye!")
            break

if __name__ == '__main__':
    main()
