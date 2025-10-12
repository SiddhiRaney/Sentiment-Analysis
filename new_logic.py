from textblob import TextBlob
import random

NEUTRAL_EMOJIS = ["😐", "🤔", "🙃", "😶", "🧐"]
NEUTRAL_MESSAGES = ["Neutral", "Mixed feelings", "Balanced view", "Could go either way", "Ambiguous"]

def classify_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return "Positive", "😊"
    elif polarity < 0:
        return "Negative", "😞"
    return random.choice(NEUTRAL_MESSAGES), random.choice(NEUTRAL_EMOJIS)

def main():
        text = input("Enter a sentence for sentiment analysis: ").strip()
        if not text:
            print("No text provided. Please try again.")
            return
        label, emoji = classify_sentiment(text)
        print(f"Sentiment: {label} {emoji}")

if __name__ == "__main__":
    main()
