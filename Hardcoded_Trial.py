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
    # Expanded list with 25 additional samples
    sample_texts = [
        "I love coding, it's amazing!",             
        "I hate bugs, they ruin everything.",       
        "Oh great, another bug to fix!",           
        "This is a regular sentence with no bias.", 
        "Absolutely fantastic experience!",        
        "I am extremely disappointed with this.",  
        "Yeah, right, that was super helpful!",    
        "I feel okay about this situation.",       
        "What a wonderful day to be alive!",       
        "This is the worst thing ever.",           
        "Oh sure, because that worked so well last time.", 
        "The book was neither good nor bad.",      
        "Best decision I have ever made!",         
        "I regret ever doing this.",               
        "Wow, such a brilliant idea... not!",      
        "It's just another normal day.",          
        "Life is beautiful and full of joy!",      
        "Nothing ever goes right for me.",         
        "Oh fantastic, another meeting at 7 AM.", 
        "Meh, it's just fine.",                    
        "My heart is filled with love and happiness!",  
        "The food was absolutely terrible.",  
        "Oh sure, because I totally wanted my coffee spilled on me.",  
        "The movie was incredibly boring, I almost fell asleep.",  
        "You are the best friend I could ever ask for!",  
        "Oh wow, another traffic jam, just what I needed!",  
        "The sunset was breathtaking, what a sight!",  
        "I can’t believe I waited this long for such a terrible service.",  
        "Oh yeah, because standing in line for hours is so much fun!",  
        "I’m feeling super productive today!",  
        "Everything is falling apart in my life right now.",  
        "Oh joy, another power cut during my favorite show!",  
        "This app is so intuitive and easy to use!",  
        "I’m extremely frustrated with how things turned out.",  
        "Oh yes, because everyone loves getting ignored.",  
        "The new update made this game even better!",  
        "Wow, that’s exactly what I wanted to hear... not!",  
        "I’m so grateful for all the opportunities in my life!",  
        "This is the most ridiculous thing I’ve ever seen.",  
        "Oh perfect, another deadline moved up!",  
        "The concert was an unforgettable experience!",  
        "Why does everything have to be so difficult?",  
        "Oh splendid, more work to do over the weekend!",  
        "I’m feeling incredibly motivated today!",  
        "I wish I never had to deal with this again.",  
        "Oh yes, because technical errors are my favorite thing ever.",  
        "The kindness of strangers always restores my faith in humanity.",  
        "This is hands down the worst customer service I’ve ever experienced.",  
    ]
    
    analyzer = SentimentAnalyzer()
    
    # Analyze each text and display results
    for text in sample_texts:
        result = analyzer.analyze(text)
        print(f"Text: {text}\nSentiment: {result['sentiment']}\nScores: {result}\n")
