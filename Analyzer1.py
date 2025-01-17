#nltk toolikit- VADER is used
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

#Comment is any piece of text/information for which we want to analyze the sentiment
def analyze_sentiment(comment):
    sentiment_scores = sia.polarity_scores(comment)

    # Interpreting the sentiment
    if sentiment_scores['compound'] >= 0.05:
        sentiment = 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    # Check if the tone is sarcastic based on sentiment polarity score and context
    sarcasm_detection = 'Sarcastic' if 'not' in comment or 'sure' in comment else 'Not Sarcastic'

    return sentiment, sarcasm_detection, sentiment_scores['compound']

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
