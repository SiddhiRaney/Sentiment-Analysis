def classify_sentiment(sentence):
    positive_words = {"love", "amazing", "fantastic", "wonderful", "best", "joy", "happiness", "grateful", "motivated", "beautiful", "breathtaking", "excited", "brilliant", "intuitive", "unforgettable"}
    negative_words = {"hate", "worst", "terrible", "regret", "disappointed", "boring", "frustrated", "ridiculous", "difficult", "falling apart", "awful", "annoying", "horrible"}
    sarcastic_clues = {"oh great", "oh sure", "yeah right", "oh wow", "oh fantastic", "oh joy", "splendid", "just what I needed", "exactly what I wanted", "oh yes"}
    
    sentence_lower = sentence.lower()
    
    if any(phrase in sentence_lower for phrase in sarcastic_clues):
        return "Sarcastic 😏"
    elif any(word in sentence_lower for word in positive_words):
        return "Positive 😊"
    elif any(word in sentence_lower for word in negative_words):
        return "Negative 😞"
    else:
        return "Neutral 😐"

sentences = [
    "I love coding, it's amazing!",  # Positive 😊
    "I hate bugs, they ruin everything.",  # Negative 😞
    "Oh great, another bug to fix!",  # Sarcastic 😏
    "This is a regular sentence with no bias.",  # Neutral 😐
    "Absolutely fantastic experience!",  # Positive 😊
    "I am extremely disappointed with this.",  # Negative 😞
    "Yeah, right, that was super helpful!",  # Sarcastic 😏
    "I feel okay about this situation.",  # Neutral 😐
    "What a wonderful day to be alive!",  # Positive 😊
    "This is the worst thing ever.",  # Negative 😞
    "Oh sure, because that worked so well last time.",  # Sarcastic 😏
    "The book was neither good nor bad.",  # Neutral 😐
    "Best decision I have ever made!",  # Positive 😊
    "I regret ever doing this.",  # Negative 😞
    "Wow, such a brilliant idea... not!",  # Sarcastic 😏
    "It's just another normal day.",  # Neutral 😐
    "Life is beautiful and full of joy!",  # Positive 😊
    "Nothing ever goes right for me.",  # Negative 😞
    "Oh fantastic, another meeting at 7 AM.",  # Sarcastic 😏
    "Meh, it's just fine.",  # Neutral 😐
    "My heart is filled with love and happiness!",  # Positive 😊
    "The food was absolutely terrible.",  # Negative 😞
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
]

# Classify and print results
for sentence in sentences:
    sentiment = classify_sentiment(sentence)
    print(f'"{sentence}"  # {sentiment}')
