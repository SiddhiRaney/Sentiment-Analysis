import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download necessary dataset
nltk.download('vader_lexicon')

# Initialize Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Sample text
text = "I love coding, it's amazing!"

# Perform sentiment analysis
sentiment_score = sia.polarity_scores(text)

# Output the results
print(sentiment_score)
