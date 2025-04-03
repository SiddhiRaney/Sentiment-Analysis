if __name__ == "__main__":
    # Mixed sample texts
    sample_texts = [
        "1. I love coding, it's amazing!",  # Positive
        "2. Absolutely fantastic experience!",  # Positive
        "3. Oh look, the ‘skip ad’ button appears just as the ad is about to end. How convenient!",  # Sarcastic
        "4. The food was absolutely terrible.",  # Negative
        "5. I received an unexpected compliment, made my day!",  # Positive
        "6. Oh joy, my favorite app just updated and now nothing works like it used to.",  # Sarcastic
        "7. I feel okay about this situation.",  # Neutral
        "8. My heart is filled with love and happiness!",  # Positive
        "9. Oh joy, another software update that changes everything for no reason.",  # Sarcastic
        "10. I wish I never had to deal with this again.",  # Negative
        "11. This book changed my perspective on life!",  # Positive
        "12. The Wi-Fi is down again, just when I needed it the most.",  # Negative
        "13. The sunset was breathtaking, what a sight!",  # Positive
        "14. Nothing beats spending time with family and friends!",  # Positive
        "15. Because nothing makes a Monday morning better than spilling coffee on my shirt.",  # Sarcastic
        "16. The test results were as expected.",  # Neutral
        "17. This article was informative but nothing groundbreaking.",  # Neutral
        "18. Oh look, my laptop battery is at 5% and my charger is conveniently in another room.",  # Sarcastic
        "19. I regret ever doing this.",  # Negative
        "20. This app is so intuitive and easy to use!",  # Positive
        "21. Oh fantastic, another meeting at 7 AM.",  # Sarcastic
        "22. Today was one of the best days of my life!",  # Positive
        "23. I’m feeling super productive today!",  # Positive
        "24. Oh wonderful, another lecture on things I already know.",  # Sarcastic
        "25. I successfully finished my project ahead of schedule!",  # Positive
        "26. Oh sure, let’s all pretend like deadlines don’t exist!",  # Sarcastic
        "27. What a beautiful time for my car to run out of fuel—right in the middle of nowhere.",  # Sarcastic
        "28. I hate bugs, they ruin everything.",  # Negative
        "29. I failed the test even after studying so hard.",  # Negative
        "30. The restaurant had the best food ever!",  # Positive
        "31. The meeting was pointless, what a waste of time.",  # Negative
        "32. The weather is fine today.",  # Neutral
        "33. Oh joy, another power cut during my favorite show!",  # Sarcastic
        "34. This project turned out way better than expected!",  # Positive
        "35. Oh yes, because everyone loves getting ignored.",  # Sarcastic
        "36. My flight got delayed again, this is frustrating.",  # Negative
        "37. Oh great, another bug to fix!",  # Sarcastic
        "38. I just got a rejection email, this sucks.",  # Negative
        "39. Oh great, my Wi-Fi disconnected right before I submitted my assignment.",  # Sarcastic
        "40. My pet just did something adorable again!",  # Positive
        "41. Because nothing makes traffic more enjoyable than the guy who cuts in last minute.",  # Sarcastic
        "42. The kindness of strangers always restores my faith in humanity.",  # Positive
        "43. I watched a movie yesterday, it was alright.",  # Neutral
        "44. The commute today was the same as every day.",  # Neutral
        "45. My favorite artist just released a new song!",  # Positive
        "46. Oh perfect, another deadline moved up!",  # Sarcastic
        "47. Oh great, my headphones tangled themselves while sitting perfectly still in my bag.",  # Sarcastic
        "48. My favorite show got canceled, I’m so upset.",  # Negative
        "49. Yes, please explain the joke to me. I totally didn’t get it the first time.",  # Sarcastic
        "50. Life is beautiful and full of joy!",  # Positive
        "51. This is hands down the worst customer service I’ve ever experienced.",  # Negative
        "52. The book was neither good nor bad.",  # Neutral
        "53. Oh wow, another traffic jam, just what I needed!",  # Sarcastic
        "54. This new policy makes everything so complicated.",  # Negative
        "55. I dropped my phone and now the screen is shattered.",  # Negative
        "56. The store had everything I needed, nothing more, nothing less.",  # Neutral
        "57. The concert was an unforgettable experience!",  # Positive
        "58. Best decision I have ever made!",  # Positive
        "59. Oh yeah, because standing in line for hours is so much fun!",  # Sarcastic
        "60. I neither liked nor disliked the movie.",  # Neutral
        "61. I just got promoted, I’m so happy!",  # Positive
        "62. This is a regular sentence with no bias.",  # Neutral
        "63. The presentation went as planned.",  # Neutral
        "64. Oh joy, another traffic jam during rush hour!",  # Sarcastic
        "65. This book changed my perspective on life!",  # Positive
        "66. The meeting ended on time, nothing unusual.",  # Neutral
        "67. Oh yeah, because I totally wanted my coffee spilled on me.",  # Sarcastic
        "68. The restaurant had the best food ever!",  # Positive
        "69. Oh sure, because I totally wanted my phone battery to die.",  # Sarcastic
        "70. I am extremely disappointed with this.",  # Negative
        "71. What a fantastic time for my phone alarm to decide not to go off!",  # Sarcastic
        "72. Meh, it's just fine.",  # Neutral
        "73. I got a perfect score on my exam, so proud of myself!",  # Positive
        "74. The food was okay, not great but not terrible.",  # Neutral
        "75. This new update made this game even better!",  # Positive
        "76. Oh wow, another delay at the airport, how surprising!",  # Sarcastic
        "77. Finally accomplished my goal—what a great feeling!",  # Positive
        "78. I have so much work and no energy to do it.",  # Negative
        "79. Waking up feeling refreshed is the best feeling ever!",  # Positive
        "80. I’m feeling incredibly motivated today!",  # Positive
        "81. Oh sure, because that worked so well last time.",  # Sarcastic
        "82. Absolutely fantastic experience!",  # Positive
        "83. I just completed my daily routine as usual.",  # Neutral
        "84. Oh fantastic, another mandatory meeting.",  # Sarcastic
        "85. I received an unexpected compliment, made my day!",  # Positive
        "86. I’m so grateful for all the opportunities in my life!",  # Positive
        "87. Oh look, another software update that changes everything for no reason.",  # Sarcastic
        "88. Yes, I’d love to hear about your vacation while I sit here drowning in work!",  # Sarcastic
        "89. This is the worst thing ever.",  # Negative
        "90. The new season of my favorite show is amazing!",  # Positive
        "91. I have never been more bored in my life.",  # Negative
        "92. My boss gave me a raise today!",  # Positive
        "93. I forgot my umbrella and now it's pouring rain.",  # Negative
        "94. I just won a contest!",  # Positive
        "95. My coffee tastes amazing today.",  # Positive
        "96. Another work email on a Sunday? Lovely.",  # Sarcastic
        "97. My pet keeps making me laugh!",  # Positive
        "98. Oh sure, cancel plans last minute, I love that.",  # Sarcastic
        "99. Just another normal day.",  # Neutral
        "100. Finally finished my to-do list!",  # Positive
    ]

    analyzer = SentimentAnalyzer()

    # Analyze each text and display results
    for text in sample_texts:
        result = analyzer.analyze(text)
        print(f"Text: {text}\nSentiment: {result['sentiment']}\nScores: {result}\n")
