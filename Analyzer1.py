import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Function to analyze sentiment
def analyze_sentiment(comment):
    sentiment_scores = sia.polarity_scores(comment)
    #calc

    # Determine the general sentiment based on compound score
    compound = sentiment_scores['compound']
    if compound >= 0.05:
        sentiment = 'Positive'
    elif compound <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    # Determine tone based on sentiment and specific scores
    tone = determine_tone(sentiment_scores)

    # Detect sarcasm (basic heuristic)
    sarcasm_detection = 'Sarcastic' if 'not' in comment.lower() or 'sure' in comment.lower() else 'Not Sarcastic'

    return sentiment, tone, sarcasm_detection, compound

# Function to determine tone
def determine_tone(scores):
    if scores['pos'] > 0.7:
        return 'Excited'
    elif scores['neg'] > 0.7:
        return 'Angry'
    elif scores['neu'] > 0.9:
        return 'Calm'
    elif scores['pos'] > scores['neg']:
        return 'Happy'
    elif scores['neg'] > scores['pos']:
        return 'Sad'
    else:
        return 'Mixed'

# Main loop
def main():
    while True:
        comment = input("Enter a comment: ").strip()
        
        # Validate input
        if not comment:
            print("Please enter a valid comment!")
            continue

        # Analyze the comment
        sentiment, tone, sarcasm, compound_score = analyze_sentiment(comment)

        # Output results
        print(f"\nComment: {comment}")
        print(f"General Sentiment: {sentiment}")
        print(f"Tone: {tone}")
        print(f"Sarcasm Detection: {sarcasm}")
        print(f"Sentiment Score (Compound): {compound_score:.2f}\n")

        # Ask if the user wants to continue
        continue_input = input("Do you want to continue (Y/N)? ").strip().lower()
        if continue_input != 'y':
            print("Exiting the program...")
            break

# Run the program
if __name__ == "__main__":
    main()
