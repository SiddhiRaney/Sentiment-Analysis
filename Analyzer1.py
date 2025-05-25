import re
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize VADER once
def init_analyzer():
    nltk.download('vader_lexicon', quiet=True)
    return SentimentIntensityAnalyzer()

sia = init_analyzer()

# Precompile sarcasm regex patterns for efficiency
SARCASTIC_PATTERNS = [re.compile(p, re.IGNORECASE) for p in [
    r"\bnot\b.*\bgood\b",
    r"\bsure\b",
    r"yeah right",
    r"totally\b.*(awesome|great)",
]]

def analyze_sentiment(text):
    """Return sentiment label, tone, sarcasm flag, and compound score."""
    scores = sia.polarity_scores(text)
    c = round(scores['compound'], 2)

    # Determine sentiment category
    if c >= 0.05:
        sentiment = 'Positive'
    elif c <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    # Assign tone based on dominant score
    pos, neg, neu = scores['pos'], scores['neg'], scores['neu']
    if pos >= 0.7:
        tone = 'Excited'
    elif neg >= 0.7:
        tone = 'Angry'
    elif neu >= 0.9:
        tone = 'Calm'
    else:
        tone = 'Happy' if pos > neg else 'Sad'

    # Check for sarcasm patterns
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
