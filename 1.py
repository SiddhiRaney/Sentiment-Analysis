import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download vader_lexicon if not already done
nltk.download('vader_lexicon')

# Initialize the VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(comment):
    # Analyze sentiment using VADER
    sentiment_scores = sia.polarity_scores(comment)

    # Interpret the sentiment
    sentiment = (
        'Positive' if sentiment_scores['compound'] >= 0.05 else
        'Negative' if sentiment_scores['compound'] <= -0.05 else
        'Neutral'
    )

    # Check if the tone is sarcastic based on certain keywords
    sarcasm_detection = 'Sarcastic' if any(word in comment for word in ['not', 'sure']) else 'Not Sarcastic'

    return sentiment, sarcasm_detection, sentiment_scores['compound']

# User Input Loop
while True:
    comment = input("Enter a comment: ")
    
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
