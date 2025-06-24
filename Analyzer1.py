import re
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Setup
nltk.download('vader_lexicon', quiet=True)
sia = SentimentIntensityAnalyzer()

# Precompiled sarcasm patterns
SARCASTIC_PATTERNS = [re.compile(p, re.IGNORECASE) for p in [
    r"\bnot\b.*\bgood\b", r"\bsure\b", r"yeah right", r"totally\b.*(awesome|great)"
]]

def analyze_sentiment(text):
    """Analyze sentiment, tone, sarcasm, and compound score."""
    scores = sia.polarity_scores(text)
    c = round(scores['compound'], 2)
    sentiment = 'Positive' if c >= 0.05 else 'Negative' if c <= -0.05 else 'Neutral'
    
    pos, neg, neu = scores['pos'], scores['neg'], scores['neu']
    tone = ('Excited' if pos >= 0.7 else 'Angry' if neg >= 0.7 
            else 'Calm' if neu >= 0.9 else 'Happy' if pos > neg else 'Sad')

    sarcasm = 'Sarcastic' if any(p.search(text) for p in SARCASTIC_PATTERNS) else 'Not Sarcastic'
    
    return sentiment, tone, sarcasm, c

if __name__ == '__main__':
    while True:
        text = input("Enter text ('exit' to quit): ").strip()
        if text.lower() == 'exit':
            print('Goodbye!')
            break
        if not text:
            print('Please enter valid text.')
            continue

        sent, tone, sarcasm, score = analyze_sentiment(text)
        print(f"Sentiment: {sent}, Tone: {tone}, Sarcasm: {sarcasm}, Score: {score}\n")
