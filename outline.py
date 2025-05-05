from textblob import TextBlob

# Input from user
text = input("Enter a sentence for sentiment analysis: ")

# Create TextBlob object
blob = TextBlob(text)

# Get sentiment polarity
polarity = blob.sentiment.polarity

# Classify sentiment
if polarity > 0:
    print("Sentiment: Positive 😊")
elif polarity < 0:
    print("Sentiment: Negative 😞")
else:
    print("Sentiment: Neutral 😐")
