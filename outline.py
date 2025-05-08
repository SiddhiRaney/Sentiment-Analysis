from textblob import TextBlob

def classify_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    return (
        ("Positive", "😊") if polarity > 0 else
        ("Negative", "😞") if polarity < 0 else
        ("Neutral", "😐")
    )

if __name__ == "__main__":
    text = input("Enter a sentence for sentiment analysis: ").strip()
    print(f"Sentiment: {label} {emoji}" if text else "No text provided. Please try again.")
    if text:
        label, emoji = classify_sentiment(text)
        print(f"Sentiment: {label} {emoji}")
