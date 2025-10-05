import fitz  # PyMuPDF

def extract_text_from_pdf(file_storage):
    """
    Reads PDF from uploaded FileStorage and returns extracted text
    """
    file_bytes = file_storage.read()
    doc = fitz.open(stream=file_bytes, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text() + " "
    return text.strip()
