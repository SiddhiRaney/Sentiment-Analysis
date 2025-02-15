import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import re

# Download necessary data
nltk.download('vader_lexicon', quiet=True)

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Precompile sarcasm patterns
SARCASM_PATTERNS = [
    re.compile(pattern, re.IGNORECASE) for pattern in (
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
    )
]

def analyze_sentiment(comment: str):
    """Analyzes sentiment and detects sarcasm in a given comment."""
    scores = sia.polarity_scores(comment)
    compound = scores['compound']
    
    sentiment = 'Positive' if compound >= 0.05 else 'Negative' if compound <= -0.05 else 'Neutral'
    sarcasm = 'Sarcastic' if any(pattern.search(comment) for pattern in SARCASM_PATTERNS) else 'Not Sarcastic'
    
    return {
        "Comment": comment,
        "Sentiment": sentiment,
        "Sarcasm Detection": sarcasm,
        "Sentiment Score": round(compound, 2),
        "Scores": {k: round(v, 2) for k, v in scores.items() if k in ('pos', 'neu', 'neg')}
    }

def main():
    """Interactive loop for sentiment analysis."""
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
                print("  - Scores:")
                for sub_key, sub_value in value.items():
                    print(f"    * {sub_key.capitalize()}: {sub_value}")
            else:
                print(f"{key}: {value}")
        print("============================\n")
        
        if input("Analyze another comment? (Y/N): ").strip().lower() != 'y':
            print("Goodbye!")
            break

if __name__ == '__main__':
    main()
