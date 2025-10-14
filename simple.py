import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download required dataset
nltk.download('vader_lexicon', quiet=True)

class SentimentAnalyzer:
    """Wrapper around NLTK's SentimentIntensityAnalyzer."""
    
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()

    def analyze(self, txt):
        """Return sentiment scores for the given text."""
        return self.sia.polarity_scores(txt)

if __name__ == "__main__":
    sa = SentimentAnalyzer()
    text = "I love coding, it's amazing!"
    
    # Perform sentiment analysis
    scores = sa.analyze(text)
    
    # Display results
    print(f"Sentiment Analysis: {scores}")
