import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Ensure the necessary dataset is available
nltk.download('vader_lexicon', quiet=True)

class SentimentAnalyzer:
    """A simple wrapper around NLTK's SentimentIntensityAnalyzer."""
    
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()

    def analyze(self, text):
        """Returns sentiment scores for the given text."""
        return self.sia.polarity_scores(text)

if __name__ == "__main__":
    analyzer = SentimentAnalyzer()
    sample_text = "I love coding, it's amazing!"
    
    # Perform sentiment analysis
    result = analyzer.analyze(sample_text)
    
    # Display results
    print(f"Sentiment Analysis: {result}")
