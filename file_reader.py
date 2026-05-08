import PyPDF2

def read_file(path):

    if path.endswith(".txt"):
        with open(path, "r", encoding="utf-8") as file:
            return file.read()

    elif path.endswith(".pdf"):
        text = ""

        with open(path, "rb") as file:
            reader = PyPDF2.PdfReader(file)

            for page in reader.pages:
                text += page.extract_text()

        return text

    else:
        raise ValueError("Unsupported file type")