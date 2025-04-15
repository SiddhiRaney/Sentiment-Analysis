if __name__ == "__main__":
    sample_texts = [
        "I love coding, it's amazing!",
        "Absolutely fantastic experience!",
        "Oh look, the ‘skip ad’ button appears just as the ad is about to end. How convenient!",
        "The food was absolutely terrible.",
        "I received an unexpected compliment, made my day!",
        "Oh joy, my favorite app just updated and now nothing works like it used to.",
        "I feel okay about this situation.",
        "My heart is filled with love and happiness!",
        "Oh joy, another software update that changes everything for no reason.",
        "I wish I never had to deal with this again.",
        # ... (same as your remaining 90 texts)
        "Finally finished my to-do list!",
    ]

    analyzer = SentimentAnalyzer()  # Initialize once

    for idx, text in enumerate(sample_texts, start=1):
        result = analyzer.analyze(text)
        sentiment = result.get('sentiment', 'Unknown')
        print(f"{idx}. Text: {text}")
        print(f"   Sentiment: {sentiment}")
        print(f"   Scores: {result}\n")
