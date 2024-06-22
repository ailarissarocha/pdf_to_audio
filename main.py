import fitz  # PyMuPDF
from gtts import gTTS

def pdf_to_audio(pdf_path, audio_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Initialize an empty string to hold the text
    text = ""
    
    # Extract text from each page
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    
    # Close the PDF file
    pdf_document.close()
    
    # Convert the extracted text to audio
    tts = gTTS(text)
    tts.save(audio_path)
    print(f"Audio saved to {audio_path}")

#usage
pdf_path = "Flutter_Syllabus.pdf"
tts_path = "Flutter_Syllabus.mp3"
pdf_to_audio(pdf_path, tts_path)