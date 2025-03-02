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
    # Initial sample texts
    sample_texts = [
        "I love coding, it's amazing!",             # Positive 😊
        "I hate bugs, they ruin everything.",       # Negative 😞
        "Oh great, another bug to fix!",           # Sarcastic 😏
        "This is a regular sentence with no bias.", # Neutral 😐
        "Absolutely fantastic experience!",        # Positive 😊
        "I am extremely disappointed with this.",  # Negative 😞
        "Yeah, right, that was super helpful!",    # Sarcastic 😏
        "I feel okay about this situation.",       # Neutral 😐
        "What a wonderful day to be alive!",       # Positive 😊
        "This is the worst thing ever.",           # Negative 😞
        "Oh sure, because that worked so well last time.", # Sarcastic 😏
        "The book was neither good nor bad.",      # Neutral 😐
        "Best decision I have ever made!",         # Positive 😊
        "I regret ever doing this.",               # Negative 😞
        "Wow, such a brilliant idea... not!",      # Sarcastic 😏
        "It's just another normal day.",          # Neutral 😐
        "Life is beautiful and full of joy!",      # Positive 😊
        "Nothing ever goes right for me.",         # Negative 😞
        "Oh fantastic, another meeting at 7 AM.", # Sarcastic 😏
        "Meh, it's just fine.",                    # Neutral 😐
        "My heart is filled with love and happiness!",  # Positive 😊
        "The food was absolutely terrible.",       # Negative 😞
        "Oh sure, because I totally wanted my coffee spilled on me.",  # Sarcastic 😏
        "The movie was incredibly boring, I almost fell asleep.",  # Negative 😞
        "You are the best friend I could ever ask for!",  # Positive 😊
        "Oh wow, another traffic jam, just what I needed!",  # Sarcastic 😏
        "The sunset was breathtaking, what a sight!",  # Positive 😊
        "I can’t believe I waited this long for such a terrible service.",  # Negative 😞
        "Oh yeah, because standing in line for hours is so much fun!",  # Sarcastic 😏
        "I’m feeling super productive today!",  # Positive 😊
        "Everything is falling apart in my life right now.",  # Negative 😞
        "Oh joy, another power cut during my favorite show!",  # Sarcastic 😏
        "This app is so intuitive and easy to use!",  # Positive 😊
        "I’m extremely frustrated with how things turned out.",  # Negative 😞
        "Oh yes, because everyone loves getting ignored.",  # Sarcastic 😏
        "The new update made this game even better!",  # Positive 😊
        "Wow, that’s exactly what I wanted to hear... not!",  # Sarcastic 😏
        "I’m so grateful for all the opportunities in my life!",  # Positive 😊
        "This is the most ridiculous thing I’ve ever seen.",  # Negative 😞
        "Oh perfect, another deadline moved up!",  # Sarcastic 😏
        "The concert was an unforgettable experience!",  # Positive 😊
        "Why does everything have to be so difficult?",  # Negative 😞
        "Oh splendid, more work to do over the weekend!",  # Sarcastic 😏
        "I’m feeling incredibly motivated today!",  # Positive 😊
        "I wish I never had to deal with this again.",  # Negative 😞
        "Oh yes, because technical errors are my favorite thing ever.",  # Sarcastic 😏
        "The kindness of strangers always restores my faith in humanity.",  # Positive 😊
        "This is hands down the worst customer service I’ve ever experienced.",  # Negative 😞
        "Oh wonderful, another lecture on things I already know.",  # Sarcastic 😏
        "I just love waiting in long queues for hours!",  # Sarcastic 😏
        "Fantastic, my code compiled with zero errors on the first try... wait, what?",  # Sarcastic 😏
        "Oh great, my WiFi disconnected right before I submitted my assignment.",  # Sarcastic 😏
        "Why do printers always decide to break when you need them the most?",  # Negative 😞
        "Wow, I definitely needed that extra spicy sauce in my eyes.",  # Sarcastic 😏
        "Oh look, my phone's battery is at 1% just when I need GPS the most!",  # Sarcastic 😏
        "I finally finished debugging after five hours, turns out it was a missing semicolon.",  # Sarcastic 😏
        "Absolutely thrilled to be stuck in traffic on my way to an important meeting!",  # Sarcastic 😏
        "Oh sure, let's all pretend like deadlines don't exist!",  # Sarcastic 😏
        "What a magnificent time to realize I left my wallet at home.",  # Sarcastic 😏
        "Oh joy, another software update that changes everything for no reason.",  # Sarcastic 😏
        "Because nothing says ‘good morning’ like stepping on a Lego.",  # Sarcastic 😏
    ]

    analyzer = SentimentAnalyzer()

    # Analyze each text and display results
    for text in sample_texts:
        result = analyzer.analyze(text)
        print(f"Text: {text}\nSentiment: {result['sentiment']}\nScores: {result}\n")
