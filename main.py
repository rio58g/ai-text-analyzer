from summarizer import summarize_text
from keypoints import extract_key_points

def main():
    print("=== AI Text Analyzer ===")
    text = input("Enter your text:\n")

    summary = summarize_text(text)
    key_points = extract_key_points(text)

    print("\n--- SUMMARY ---")
    print(summary)

    print("\n--- KEY POINTS ---")
    for point in key_points:
        print(f"- {point}")

if __name__ == "__main__":
    main()