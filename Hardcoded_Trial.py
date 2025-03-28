if __name__ == "__main__":
    # Initial sample texts
    sample_texts = [
        # Positive 😊
        "1. I love coding, it's amazing!",  
        "2. Absolutely fantastic experience!",  
        "3. What a wonderful day to be alive!",  
        "4. Best decision I have ever made!",  
        "5. Life is beautiful and full of joy!",  
        "6. My heart is filled with love and happiness!",  
        "7. The sunset was breathtaking, what a sight!",  
        "8. I’m feeling super productive today!",  
        "9. This app is so intuitive and easy to use!",  
        "10. The new update made this game even better!",  
        "11. I’m so grateful for all the opportunities in my life!",  
        "12. The concert was an unforgettable experience!",  
        "13. The kindness of strangers always restores my faith in humanity.",  
        "14. I’m feeling incredibly motivated today!",  
        "15. The restaurant had the best food ever!",  
        "16. This project turned out way better than expected!",  
        "17. I can’t stop smiling after hearing the good news!",  
        "18. Finally accomplished my goal—what a great feeling!",  
        "19. This book changed my perspective on life!",  
        "20. Nothing beats spending time with family and friends!",  

        # Negative 😞
        "21. I hate bugs, they ruin everything.",  
        "22. I am extremely disappointed with this.",  
        "23. This is the worst thing ever.",  
        "24. I regret ever doing this.",  
        "25. Nothing ever goes right for me.",  
        "26. The food was absolutely terrible.",  
        "27. I can’t believe I waited this long for such a terrible service.",  
        "28. Everything is falling apart in my life right now.",  
        "29. This is hands down the worst customer service I’ve ever experienced.",  
        "30. I wish I never had to deal with this again.",  
        "31. The Wi-Fi is down again, just when I needed it the most.",  
        "32. I failed the test even after studying so hard.",  
        "33. This new policy makes everything so complicated.",  
        "34. My favorite show got canceled, I’m so upset.",  
        "35. I dropped my phone and now the screen is shattered.",  
        "36. The meeting was pointless, what a waste of time.",  
        "37. I have so much work and no energy to do it.",  
        "38. I feel like I’m stuck in the same loop every day.",  
        "39. My flight got delayed again, this is frustrating.",  
        "40. I just got a rejection email, this sucks.",  

        # Sarcastic 😏
        "41. Oh great, another bug to fix!",  
        "42. Yeah, right, that was super helpful!",  
        "43. Oh sure, because that worked so well last time.",  
        "44. Wow, such a brilliant idea... not!",  
        "45. Oh fantastic, another meeting at 7 AM.",  
        "46. Oh sure, because I totally wanted my coffee spilled on me.",  
        "47. Oh yeah, because standing in line for hours is so much fun!",  
        "48. Oh joy, another power cut during my favorite show!",  
        "49. Oh yes, because everyone loves getting ignored.",  
        "50. Wow, that’s exactly what I wanted to hear... not!",  
        "51. Fantastic, my code compiled with zero errors on the first try... wait, what?",  
        "52. Oh great, my WiFi disconnected right before I submitted my assignment.",  
        "53. Oh wow, another traffic jam, just what I needed!",  
        "54. Oh sure, let’s all pretend like deadlines don’t exist!",  
        "55. Oh joy, another software update that changes everything for no reason.",  
        "56. Because nothing says ‘good morning’ like stepping on a Lego.",  
        "57. Oh look, the ‘skip ad’ button appears just as the ad is about to end. How convenient!",  
        "58. Yes, I’d love to hear about your vacation while I sit here drowning in work!",  
        "59. Because nothing makes traffic more enjoyable than the guy who cuts in last minute.",  
        "60. Oh wonderful, another lecture on things I already know.",  

        # Neutral 😐
        "61. This is a regular sentence with no bias.",  
        "62. I feel okay about this situation.",  
        "63. The book was neither good nor bad.",  
        "64. It's just another normal day.",  
        "65. Meh, it's just fine.",  
        "66. The test results were as expected.",  
        "67. I neither liked nor disliked the movie.",  
        "68. It’s an average restaurant, nothing special.",  
        "69. The weather is fine today.",  
        "70. I just completed my daily routine as usual.",  
        "71. It’s another Monday, nothing new.",  
        "72. The presentation went as planned.",  
        "73. I watched a movie yesterday, it was alright.",  
        "74. It was a standard customer service experience.",  
        "75. The meeting ended on time, nothing unusual.",  
        "76. The commute today was the same as every day.",  
        "77. The food was okay, not great but not terrible.",  
        "78. I walked around the city for a bit, nothing exciting happened.",  
        "79. This article was informative but nothing groundbreaking.",  
        "80. The store had everything I needed, nothing more, nothing less.",  

        # Extra Sarcastic for fun 😏
        "81. Oh perfect, another deadline moved up!",  
        "82. Amazing! My headphones tangled themselves while sitting perfectly still in my bag.",  
        "83. What a beautiful time for my car to run out of fuel—right in the middle of nowhere.",  
        "84. Oh look, my laptop battery is at 5% and my charger is conveniently in another room.",  
        "85. Yes, let’s wait in line for 30 minutes just to be told ‘we’re out of stock’!",  
        "86. Oh joy, my favorite app just updated and now nothing works like it used to.",  
        "87. Because nothing makes a Monday morning better than spilling coffee on my shirt.",  
        "88. Oh great, my Wi-Fi slowed down the moment I actually needed it to work.",  
        "89. Yes, please explain the joke to me. I totally didn’t get it the first time.",  
        "90. What a fantastic time for my phone alarm to decide not to go off!",  

        # Extra Positive to balance 😊
        "91. I just got promoted, I’m so happy!",  
        "92. Today was one of the best days of my life!",  
        "93. I received an unexpected compliment, made my day!",  
        "94. I love the new season of my favorite show!",  
        "95. My pet just did something adorable again!",  
        "96. I successfully finished my project ahead of schedule!",  
        "97. I had an amazing time catching up with old friends!",  
        "98. I got a perfect score on my exam, so proud of myself!",  
        "99. My favorite artist just released a new song!",  
        "100. Waking up feeling refreshed is the best feeling ever!",  
    ]

    analyzer = SentimentAnalyzer()

    # Analyze each text and display results
    for text in sample_texts:
        result = analyzer.analyze(text)
        print(f"Text: {text}\nSentiment: {result['sentiment']}\nScores: {result}\n")
