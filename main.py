import argparse
from summarizer import summarize_text
from keypoints import extract_key_points
from sentiment import analyze_sentiment
from file_reader import read_file
from exporter import save_to_markdown

def main():
    parser = argparse.ArgumentParser(description="AI Text Analyzer v2")
    parser.add_argument("--files", nargs="+", help="Multiple files")

    args = parser.parse_args()

    texts = []

    if args.files:
        for file in args.files:
            texts.append(read_file(file))

        text = "\n".join(texts)

    else:
        text = input("Enter your text:\n")

    print("\nAnalyzing...\n")

    summary = summarize_text(text)
    keypoints = extract_key_points(text)
    sentiment = analyze_sentiment(text)

    print("\n--- SUMMARY ---")
    print(summary)

    print("\n--- KEY POINTS ---")
    for point in keypoints:
        print(f"- {point}")

    print("\n--- SENTIMENT ---")
    print(sentiment)

    saved_file = save_to_markdown(summary, keypoints, sentiment)

    print(f"\nResults saved to: {saved_file}")

if __name__ == "__main__":
    main()