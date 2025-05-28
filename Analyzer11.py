import re  # for regex operations
import textwrap  # for formatting long text outputs
type Dict, Any from typing  # for type hints
from transformers import pipeline  # to load pre-trained NLP models

# Initialize Hugging Face sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Pre-compiled regex patterns for basic sarcasm detection
sarcasm_patterns = [
    re.compile(pat, re.IGNORECASE)
    for pat in [r"yeah,? right", r"totally\s.*", r"as if"]
]

def analyze_sentiment(comment: str) -> Dict[str, Any]:
    """
    Analyze a comment to determine sentiment, tone, and basic sarcasm.

    Args:
        comment (str): The input text to analyze.

    Returns:
        Dict[str, Any]: A dictionary with keys:
            - sentiment: 'Positive' or 'Negative'
            - tone: 'Excited', 'Angry', or 'Neutral'
            - sarcasm: 'Sarcastic' or 'Not Sarcastic'
            - score: dict with raw model label and confidence score
    """
    try:
        # Run the sentiment analysis model
        result = sentiment_pipeline(comment)[0]
        label = result['label']  # 'POSITIVE' or 'NEGATIVE'
        score = result['score']  # confidence score

        # Determine high-level sentiment
        sentiment = "Positive" if label == "POSITIVE" else "Negative"

        # Assign a tone based on confidence thresholds
        if label == "POSITIVE" and score > 0.9:
            tone = "Excited"
        elif label == "NEGATIVE" and score > 0.9:
            tone = "Angry"
        else:
            tone = "Neutral"

        # Simple sarcasm check using regex patterns
        sarcasm = (
            "Sarcastic"
            if any(p.search(comment) for p in sarcasm_patterns)
            else "Not Sarcastic"
        )

        # Round score for readability
        return {
            "sentiment": sentiment,
            "tone": tone,
            "sarcasm": sarcasm,
            "score": {"label": label, "score": round(score, 2)},
        }
    except Exception as e:
        # Return any errors encountered during analysis
        return {"error": str(e)}


def display_results(comment: str, result: Dict[str, Any]) -> None:
    """
    Nicely print the analysis results to the console.

    Args:
        comment (str): The original input text.
        result (Dict[str, Any]): The analysis output from analyze_sentiment.
    """
    print("\n" + "-" * 50)
    print("Comment:")
    # Wrap long comments for better console display
    print(textwrap.fill(comment, width=50))
    print()

    # Iterate through result dict and print details
    for key, value in result.items():
        if isinstance(value, dict):
            print("Score Breakdown:")
            for sub_key, sub_value in value.items():
                print(f"  {sub_key.capitalize()}: {sub_value}")
        else:
            print(f"{key.capitalize()}: {value}")
    print("-" * 50 + "\n")


def main() -> None:
    """
    Entry point for the sentiment analysis tool.
    Continuously prompt the user for input until 'exit' is entered.
    """
    print("Welcome to the Sentiment Analysis Tool!")
    while True:
        comment = input("Enter a comment (or type 'exit' to quit): ")
        # Exit condition
        if comment.strip().lower() == 'exit':
            print("Exiting the program...")
            break
        # Handle empty input
        if not comment.strip():
            print("Error: Please enter a valid comment!")
            continue
        # Analyze and display results
        result = analyze_sentiment(comment)
        if "error" in result:
            print(f"Error: {result['error']}")
        else:
            display_results(comment, result)


if __name__ == "__main__":
    main()
