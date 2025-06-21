import fitz  # PyMuPDF
import pytesseract
from pdf2image import convert_from_bytes
from PIL import Image

def extract_text_from_pdf(uploaded_file):
    """Extracts text from a PDF. Falls back to OCR for scanned PDFs."""
    text = ""

    # Step 1: Try PyMuPDF extraction
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        for page in doc:
            page_text = page.get_text()
            text += page_text

    # Step 2: If text is too short, fallback to OCR
    if len(text.strip()) < 50:
        print("Fallback to OCR - scanned PDF detected.")
        uploaded_file.seek(0)  # Reset pointer
        images = convert_from_bytes(uploaded_file.read())
        ocr_text = ""

        for img in images:
            gray = img.convert("L")  # grayscale
            ocr_text += pytesseract.image_to_string(gray)

        return ocr_text
    else:
        return text
