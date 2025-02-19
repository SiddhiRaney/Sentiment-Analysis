import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import re

# Download required NLTK data quietly
nltk.download('vader_lexicon', quiet=True)

# Initialize Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Expanded sarcasm patterns
SARCASM_PATTERNS = [
    re.compile(pattern, re.IGNORECASE) for pattern in (
        r'not\s+(great|good|bad|terrible|happy|sad|funny|helpful)',
        r'yeah\s+right|sure\s+thing',
        r'totally\s+(agree|disagree|true|false|believable)',
        r'as\s+if|oh\s+really|obviously',
        r'wow\s+(amazing|incredible|fantastic|horrible)',
        r'just\s+what\s+I\s+needed',
        r'so\s+much\s+fun|love\s+that\s+for\s+me',
        r'what\s+a\s+(surprise|shock|joke)',
        r'nothing\s+could\s+be\s+(better|worse)',
        r'glad\s+to\s+hear\s+that'
    )
]

def detect_sarcasm(text: str) -> bool:
    """Checks if the given text matches sarcasm patterns."""
    return any(pattern.search(text) for pattern in SARCASM_PATTERNS)

def adjust_for_sarcasm(sentiment: str, sarcasm: bool) -> str:
    """Adjusts sentiment classification if sarcasm is detected."""
    if sarcasm and sentiment == 'Positive':
        return 'Negative'
    elif sarcasm and sentiment == 'Neutral':
        return 'Slightly Negative'
    return sentiment

def analyze_sentiment(text: str) -> dict:
    """Analyzes sentiment and detects sarcasm in the given text."""
    try:
        scores = sia.polarity_scores(text)
        compound = scores['compound']
        sentiment = 'Positive' if compound >= 0.05 else 'Negative' if compound <= -0.05 else 'Neutral'
        
        sarcasm_detected = detect_sarcasm(text)
        adjusted_sentiment = adjust_for_sarcasm(sentiment, sarcasm_detected)

        return {
            "Comment": text,
            "Sentiment": adjusted_sentiment,
            "Sarcasm Detection": "Sarcastic" if sarcasm_detected else "Not Sarcastic",
            "Sentiment Score": round(compound, 2),
            "Scores": {k: round(scores[k], 2) for k in ['pos', 'neu', 'neg']}
        }
    except Exception as e:
        return {"Error": f"An error occurred: {str(e)}"}

def main():
    """Runs an interactive sentiment and sarcasm analyzer."""
    print("\n=== Sentiment & Sarcasm Analyzer ===\n(Type 'exit' to quit)\n")
    
    while True:
        try:
            comment = input("Enter a comment: ").strip()
            if comment.lower() == 'exit':
                print("\nGoodbye!\n")
                break
            if not comment:
                print("\n[!] Please enter a valid comment.\n")
                continue
            
            result = analyze_sentiment(comment)
            print("\n=====================================")
            for key, value in result.items():
                if isinstance(value, dict):
                    print("  - Scores:")
                    for sub_key, sub_value in value.items():
                        print(f"    * {sub_key.capitalize()}: {sub_value}")
                else:
                    print(f"{key}: {value}")
            print("=====================================\n")
            
            if input("Analyze another comment? (Y/N): ").strip().lower() != 'y':
                print("\nGoodbye!\n")
                break
        except KeyboardInterrupt:
            print("\n[!] Process interrupted. Exiting.\n")
            break
        except Exception as e:
            print(f"\n[!] An unexpected error occurred: {str(e)}\n")

if __name__ == '__main__':
    main()
