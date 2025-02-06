import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import re

# Download vader_lexicon if not already done
nltk.download('vader_lexicon')

# Initialize the VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(comment):
    # Analyze sentiment using VADER
    sentiment_scores = sia.polarity_scores(comment)
    
    # Sentiment interpretation based on compound score
    sentiment = 'Positive' if sentiment_scores['compound'] >= 0.05 else \
               'Negative' if sentiment_scores['compound'] <= -0.05 else \
               'Neutral'
    
    # Sarcasm detection with a broader pattern set
    sarcasm_keywords = r'\b(not|no|never|barely|hardly|don\'t|isn\'t|won\'t|can\'t)\b'
    sarcasm_detection = 'Sarcastic' if re.search(sarcasm_keywords, comment, re.IGNORECASE) else 'Not Sarcastic'

    return sentiment, sarcasm_detection, sentiment_scores['compound']

# User Input Loop
def main():
    while True:
        comment = input("Enter a comment: ").strip()
        
        if not comment:  # Check if the input is empty
            print("Please enter a valid comment.")
            continue
        
        sentiment, sarcasm, compound_score = analyze_sentiment(comment)
        
        # Output Results
        print(f"\nComment: {comment}")
        print(f"Sentiment: {sentiment}")
        print(f"Sarcasm Detection: {sarcasm}")
        print(f"Sentiment Score: {compound_score:.2f}\n")

        # Ask if the user wants to continue or break
        if input("Do you want to continue (Y/N)? ").strip().lower() != 'y':
            print("Exiting the program. Goodbye!")
            break

# Run the program
if __name__ == '__main__':
    main()
