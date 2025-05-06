from textblob import TextBlob

def classify_sentiment(text):
    """
    Classifies the sentiment of the given text using TextBlob.
    Returns: A tuple (label, emoji)
    """
    polarity = TextBlob(text).sentiment.polarity
    
    if polarity > 0:
        return "Positive", "😊"
    elif polarity < 0:
        return "Negative", "😞"
    else:
        return "Neutral", "😐"

if __name__ == "__main__":
    text = input("Enter a sentence for sentiment analysis: ").strip()
    if text:
        label, emoji = classify_sentiment(text)
        print(f"Sentiment: {label} {emoji}")
    else:
        print("No text provided. Please try again.")
