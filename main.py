import argparse
from summarizer import summarize_text
from keypoints import extract_key_points
from file_reader import read_file

def main():
    parser = argparse.ArgumentParser(description="AI Text Analyzer")
    parser.add_argument("--file", help="Path to text or PDF file")
    parser.add_argument("--mode", choices=["summarize", "keypoints", "both"], default="both")
    args = parser.parse_args()

    if args.file:
        text = read_file(args.file)
    else:
        text = input("Enter your text:\n")

    if args.mode in ["summarize", "both"]:
        print("\n--- SUMMARY ---")
        print(summarize_text(text))

    if args.mode in ["keypoints", "both"]:
        print("\n--- KEY POINTS ---")
        key_points = extract_key_points(text)
        for point in key_points:
            print(f"- {point}")

if __name__ == "__main__":
    main()