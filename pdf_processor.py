import fitz

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    txt = "".join(page.get_text() for page in doc)
    return txt
