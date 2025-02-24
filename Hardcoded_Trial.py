import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download required dataset silently
nltk.download("vader_lexicon", quiet=True)

class SentimentAnalyzer:
    """Wrapper around NLTK's SentimentIntensityAnalyzer for emotion detection."""

    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze(self, text: str) -> dict:
        """
        Returns sentiment scores and classifies the sentiment type.
        
        :param text: The input text to analyze.
        :return: A dictionary containing sentiment scores and the detected sentiment.
        """
        scores = self.analyzer.polarity_scores(text)
        sentiment = self.classify_sentiment(scores)
        scores["sentiment"] = sentiment
        return scores

    def classify_sentiment(self, scores: dict) -> str:
        """
        Categorizes sentiment as Positive, Negative, Neutral, or Sarcastic.
        
        :param scores: Dictionary containing sentiment intensity scores.
        :return: A string representing the sentiment type.
        """
        pos, neg, neu, compound = scores["pos"], scores["neg"], scores["neu"], scores["compound"]

        # Define thresholds for classification
        if compound >= 0.5:
            return "Positive 😊"
        elif compound <= -0.5:
            return "Negative 😞"
        elif 0.1 < compound < 0.5 and pos > neg:
            return "Sarcastic 😏"
        else:
            return "Neutral 😐"

if __name__ == "__main__":
    # Sample texts for testing different sentiment cases
    sample_texts = [
        "I love coding, it's amazing!",             # Positive
        "I hate bugs, they ruin everything.",       # Negative
        "Oh great, another bug to fix!",           # Sarcastic
        "This is a regular sentence with no bias.", # Neutral
        "Absolutely fantastic experience!",        # Positive
        "I am extremely disappointed with this.",  # Negative
        "Yeah, right, that was super helpful!",    # Sarcastic
        "I feel okay about this situation.",       # Neutral
        "What a wonderful day to be alive!",       # Positive
        "This is the worst thing ever.",           # Negative
        "Oh sure, because that worked so well last time.", # Sarcastic
        "The book was neither good nor bad.",      # Neutral
        "Best decision I have ever made!",         # Positive
        "I regret ever doing this.",               # Negative
        "Wow, such a brilliant idea... not!",      # Sarcastic
        "It's just another normal day.",          # Neutral
        "Life is beautiful and full of joy!",      # Positive
        "Nothing ever goes right for me.",         # Negative
        "Oh fantastic, another meeting at 7 AM.", # Sarcastic
        "Meh, it's just fine.",                    # Neutral
    ]
    
    analyzer = SentimentAnalyzer()
    
    # Analyze each text and display results
    for text in sample_texts:
        result = analyzer.analyze(text)
        print(f"Text: {text}\nSentiment: {result['sentiment']}\nScores: {result}\n")
