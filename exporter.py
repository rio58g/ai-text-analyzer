import os
from datetime import datetime

def save_to_markdown(summary, keypoints, sentiment):

    os.makedirs("outputs", exist_ok=True)

    filename = f"outputs/result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"

    with open(filename, "w", encoding="utf-8") as file:

        file.write("# AI Text Analysis\n\n")

        file.write("## Summary\n")
        file.write(summary + "\n\n")

        file.write("## Key Points\n")

        for point in keypoints:
            file.write(f"- {point}\n")

        file.write("\n## Sentiment\n")
        file.write(sentiment)

    return filename