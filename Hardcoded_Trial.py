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
        "Oh wow, another meeting that could have been an email? What a delightful surprise!" # Sarcastic 😏

"Fantastic! My laptop decided to restart for updates right before my presentation." # Sarcastic 😏

"Oh, you texted me back after three days? Must have been SO hard to type ‘okay’." # Sarcastic 😏

"What an amazing time for my internet to go out—right in the middle of an important upload!" # Sarcastic 😏

"Because nothing makes me feel more alive than waking up five minutes before my alarm." # Sarcastic 😏

"Oh great, I just love when autocorrect turns my normal sentence into complete nonsense." # Sarcastic 😏

"Yes, please keep honking at traffic—I’m sure it will magically make the cars disappear!" # Sarcastic 😏

"Oh sure, let’s schedule maintenance at peak hours. Genius!" # Sarcastic 😏

"What a perfect day for my umbrella to break in the middle of a downpour." # Sarcastic 😏

"Amazing! My headphones tangled themselves while sitting perfectly still in my bag." # Sarcastic 😏

"Oh look, the ‘skip ad’ button appears just as the ad is about to end. How convenient!" # Sarcastic 😏

"Yes, I’d love to hear about your vacation while I sit here drowning in work!" # Sarcastic 😏

"Because nothing makes traffic more enjoyable than the guy who cuts in last minute." # Sarcastic 😏

"Oh wow, my phone fell screen-down. I bet it’s totally fine. No cracks at all!" # Sarcastic 😏

"Amazing! I spilled my drink exactly where I was trying to avoid spilling it." # Sarcastic 😏

"What a beautiful time for my car to run out of fuel—right in the middle of nowhere." # Sarcastic 😏

"Oh look, my laptop battery is at 5% and my charger is conveniently in another room." # Sarcastic 😏

"Yes, let’s wait in line for 30 minutes just to be told ‘we’re out of stock’!" # Sarcastic 😏

"How exciting! Another ‘urgent’ email that could have been a two-sentence message." # Sarcastic 😏

"Oh joy, my favorite app just updated and now nothing works like it used to." # Sarcastic 😏

"Because nothing makes a Monday morning better than spilling coffee on my shirt." # Sarcastic 😏

"Oh great, my Wi-Fi slowed down the moment I actually needed it to work." # Sarcastic 😏

"Yes, please explain the joke to me. I totally didn’t get it the first time." # Sarcastic 😏

"What a fantastic time for my phone alarm to decide not to go off!" # Sarcastic 😏

"Oh sure, let’s change all the grocery store aisles around just when I finally memorized them!" # Sarcastic 😏
        
    ]

    analyzer = SentimentAnalyzer()

    # Analyze each text and display results
    for text in sample_texts:
        result = analyzer.analyze(text)
        print(f"Text: {text}\nSentiment: {result['sentiment']}\nScores: {result}\n")
