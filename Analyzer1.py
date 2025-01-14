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
    if sentiment_scores['compound'] >= 0.05:
        sentiment = 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    # Check if the tone is sarcastic based on sentiment polarity score and context
    sarcasm_detection = 'Sarcastic' if 'not' in comment or 'sure' in comment else 'Not Sarcastic'

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
    continue_input = input("Do you want to continue (Y/N)? ").strip().lower()
    
    if continue_input != 'y':
        print("Exiting the program. Goodbye!")
        break
