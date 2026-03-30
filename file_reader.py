import PyPDF2

def read_file(path):
    if path.lower().endswith(".txt"):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    elif path.lower().endswith(".pdf"):
        text = ""
        with open(path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        return text
    else:
        raise ValueError("Unsupported file type. Use .txt or .pdf")