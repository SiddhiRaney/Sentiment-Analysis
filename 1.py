import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import re

# Download vader_lexicon if not already done
nltk.download('vader_lexicon', quiet=True)

# Initialize the VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(comment):
    """Analyzes sentiment and detects sarcasm in a given comment."""
    sentiment_scores = sia.polarity_scores(comment)
    
    # Determine sentiment based on compound score
    compound = sentiment_scores['compound']
    sentiment = 'Positive' if compound >= 0.05 else 'Negative' if compound <= -0.05 else 'Neutral'
    
    # Improved sarcasm detection using common sarcastic phrases and negations
    sarcasm_patterns = [
        r'(?i)not\s+(great|good|bad|terrible|happy|sad|funny)',  # Example: "Not great at all"
        r'(?i)yeah\s+right',  # Example: "Yeah, right!"
        r'(?i)sure\s+thing',  # Example: "Sure thing..."
        r'(?i)totally\s+(agree|disagree|true|false)',  # Example: "Totally agree with you (not)"
        r'(?i)as\s+if',  # Example: "As if that would happen!"
        r'(?i)oh\s+really',  # Example: "Oh really? (with sarcasm)"
        r'(?i)wow\s+(amazing|incredible|fantastic)',  # Example: "Wow, amazing work (sarcastic)"
        r'(?i)just\s+what\s+I\s+needed',  # Example: "Just what I needed!"
        r'(?i)so\s+much\s+fun',  # Example: "This is so much fun... (sarcastic)"
        r'(?i)love\s+that\s+for\s+me',  # Example: "Love that for me!"
    ]
    sarcasm_detected = any(re.search(pattern, comment) for pattern in sarcasm_patterns)
    sarcasm = 'Sarcastic' if sarcasm_detected else 'Not Sarcastic'
    
    return sentiment, sarcasm, compound, sentiment_scores

def main():
    """Runs an interactive user input loop for sentiment analysis."""
    print("Welcome to the Sentiment and Sarcasm Analyzer! Enter your comments below.")
    print("Type 'exit' to quit the program.")
    
    while True:
        comment = input("Enter a comment: ").strip()
        if comment.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        if not comment:
            print("Please enter a valid comment.")
            continue
        
        sentiment, sarcasm, compound_score, scores = analyze_sentiment(comment)
        
        print("\n============================")
        print(f"Comment: {comment}")
        print(f"Sentiment: {sentiment}")
        print(f"Sarcasm Detection: {sarcasm}")
        print(f"Sentiment Score: {compound_score:.2f}")
        print("Detailed Scores:")
        print(f"  - Positive: {scores['pos']:.2f}")
        print(f"  - Neutral: {scores['neu']:.2f}")
        print(f"  - Negative: {scores['neg']:.2f}")
        print("============================\n")
        
        if input("Do you want to analyze another comment (Y/N)? ").strip().lower() != 'y':
            print("Exiting the program. Goodbye!")
            break

if __name__ == '__main__':
    main()
