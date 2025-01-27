import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Function to analyze sentiment
def analyze_sentiment(comment):
    scores = sia.polarity_scores(comment)
    compound_score = scores['compound']
    sentiment = (
        'Positive' if compound_score >= 0.05
        else 'Negative' if compound_score <= -0.05
        else 'Neutral'
    )
    tone = determine_tone(scores)
    sarcasm = detect_sarcasm(comment)
    return sentiment, tone, sarcasm, compound_score

# Function to determine tone
def determine_tone(scores):
    pos, neg, neu = scores['pos'], scores['neg'], scores['neu']
    if pos > 0.7:
        return 'Excited'
    elif neg > 0.7:
        return 'Angry'
    elif neu > 0.9:
        return 'Calm'
    elif pos > neg:
        return 'Happy'
    elif neg > pos:
        return 'Sad'
    else:
        return 'Mixed'

# Function to detect sarcasm
def detect_sarcasm(comment):
    sarcasm_keywords = ['not', 'sure', 'yeah right', 'totally']
    return 'Sarcastic' if any(keyword in comment.lower() for keyword in sarcasm_keywords) else 'Not Sarcastic'

# Main loop
def main():
    print("Sentiment Analysis Program\nType your comments and receive sentiment insights.\n")
    
    while True:
        comment = input("Enter a comment (or type 'exit' to quit): ").strip()
        
        if comment.lower() == 'exit':
            print("Exiting the program...")
            break
        
        if not comment:
            print("Please enter a valid comment!")
            continue

        try:
            sentiment, tone, sarcasm, compound_score = analyze_sentiment(comment)
            print(f"\nComment: {comment}")
            print(f"General Sentiment: {sentiment}")
            print(f"Tone: {tone}")
            print(f"Sarcasm Detection: {sarcasm}")
            print(f"Sentiment Score (Compound): {compound_score:.2f}\n")
        except Exception as e:
            print(f"Error analyzing the comment: {e}")
            continue

        continue_input = input("Do you want to analyze another comment (Y/N)? ").strip().lower()
        if continue_input != 'y':
            print("Thank you for using the program!")
            break

# Run the program
if __name__ == "__main__":
    main()
