from textblob import TextBlob
import random

def classify_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return ("Positive", "😊")
    elif polarity < 0:
        return ("Negative", "😞")
    else:
        neutral_emojis = ["😐", "🤔", "🙃", "😶", "🧐"]
        neutral_messages = ["Neutral", "Mixed feelings", "Balanced view", "Could go either way", "Ambiguous"]
        return (random.choice(neutral_messages), random.choice(neutral_emojis))

if __name__ == "__main__":
    text = input("Enter a sentence for sentiment analysis: ").strip()
    if text:
        label, emoji = classify_sentiment(text)
        print(f"Sentiment: {label} {emoji}")
    else:
        print("No text provided. Please try again.")
