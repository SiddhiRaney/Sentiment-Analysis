import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import re

# Download required NLTK data quietly
nltk.download('vader_lexicon', quiet=True)

# Initialize Sentiment Analyzer
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

def detect_sarcasm(text: str) -> bool:
    """Checks if the given text matches any sarcasm pattern."""
    return any(pattern.search(text) for pattern in SARCASM_PATTERNS)

def analyze_sentiment(text: str) -> dict:
    """Analyzes sentiment and detects sarcasm in the given text."""
    scores = sia.polarity_scores(text)
    compound = scores['compound']
    sentiment = 'Positive' if compound >= 0.05 else 'Negative' if compound <= -0.05 else 'Neutral'
    sarcasm = 'Sarcastic' if detect_sarcasm(text) else 'Not Sarcastic'
    
    return {
        "Comment": text,
        "Sentiment": sentiment,
        "Sarcasm Detection": sarcasm,
        "Sentiment Score": round(compound, 2),
        "Scores": {k: round(v, 2) for k in ('pos', 'neu', 'neg') if k in scores}
    }

def main():
    """Runs an interactive sentiment and sarcasm analyzer."""
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
