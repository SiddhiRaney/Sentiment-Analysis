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

    # Additional hardcoded examples
    extra_texts = [
        "Oh wonderful, another lecture on things I already know.",
        "I just love waiting in long queues for hours!",
        "Fantastic, my code compiled with zero errors on the first try... wait, what?",
        "Oh great, my WiFi disconnected right before I submitted my assignment.",
        "Why do printers always decide to break when you need them the most?",
        "Wow, I definitely needed that extra spicy sauce in my eyes.",
        "Oh look, my phone's battery is at 1% just when I need GPS the most!",
        "I finally finished debugging after five hours, turns out it was a missing semicolon.",
        "Absolutely thrilled to be stuck in traffic on my way to an important meeting!",
        "Oh sure, let's all pretend like deadlines don't exist!",
        "What a magnificent time to realize I left my wallet at home.",
        "I just love how every single app needs an update at the same time.",
        "Waking up to 50 unread emails is exactly what I needed today.",
        "My dog decided my new shoes were his chew toy. How thoughtful!",
        "So nice of my alarm clock to take the day off without informing me.",
        "Oh fantastic, my laptop decided to restart right in the middle of my work.",
        "I spent an hour cooking only to realize I forgot to add salt.",
        "Oh joy, another software update that changes everything for no reason.",
        "Because nothing says ‘good morning’ like stepping on a Lego.",
        "I love how my coffee spills only when I wear white clothes.",
        "Wow, another day of pretending like I have my life together.",
        "Oh look, my meeting just got extended by another hour. Exactly what I wanted!",
        "My neighbors have decided that 2 AM is the perfect time for karaoke practice.",
        "Nothing feels better than finally understanding a concept right before the exam ends.",
        "Why does my brain decide to remind me of embarrassing moments from 10 years ago?",
        "Oh sure, because hitting ‘remind me tomorrow’ on updates always works out.",
        "I just love how my cat decides my laptop keyboard is the best nap spot.",
        "Oh yes, I definitely wanted my smoothie to explode in the blender today.",
        "Because nothing screams ‘productivity’ like accidentally deleting hours of work.",
        "Oh perfect, my phone fell face-first on concrete. Let’s check the damage together!",
        "Oh brilliant, my earphones decided to tangle themselves again.",
        "Wow, my internet is so fast, I could send a letter quicker than this.",
        "I just love how my laptop crashes at the perfect moment.",
        "Oh sure, waking up early on a Sunday is exactly what I wanted.",
        "Fantastic, my phone updated overnight and now nothing works!",
        "Why does my charger only work when I hold it at a weird angle?",
        "Oh great, my ice cream melted before I could even take a bite.",
        "I love how my pet ignores me until it’s dinner time.",
        "Oh sure, rain starts pouring the moment I step outside.",
        "Wow, I definitely needed that unexpected pop quiz today.",
        "Oh fantastic, my printer ran out of ink right before I submitted my report.",
        "Because nothing says ‘fun’ like losing my progress on a document I forgot to save.",
        "Oh yes, my phone’s autocorrect always knows exactly what I meant to type."
    ]

    # Combine both lists
    sample_texts.extend(extra_texts)

    analyzer = SentimentAnalyzer()

    # Analyze each text and display results
    for text in sample_texts:
        result = analyzer.analyze(text)
        print(f"Text: {text}\nSentiment: {result['sentiment']}\nScores: {result}\n")
