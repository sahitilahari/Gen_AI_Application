import streamlit as st
from PIL import Image
import pytesseract
from googletrans import Translator  # Ensure this is installed: pip install googletrans==4.0.0-rc1

# Tesseract OCR configuration
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Title
st.title("AI-Powered Solution for Visually Impaired Individuals")

# Upload an image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_container_width=True)

    # Extract Text
    text = pytesseract.image_to_string(img)

    if text.strip():  # Ensure text is not empty
        st.write("Extracted Text:", text)

        # Translation Section
        translator = Translator()

        # Language Selection
        source_language = st.selectbox("Select Source Language", ["auto", "en", "es", "fr", "de", "hi", "zh"])
        target_language = st.selectbox("Select Target Language", ["en", "es", "fr", "de", "hi", "zh"])

        if st.button("Translate Text"):
            with st.spinner("Translating..."):
                try:
                    translation = translator.translate(text, src=source_language, dest=target_language)
                    st.write(f"Translated Text ({target_language}):", translation.text)
                except Exception as e:
                    st.error(f"Translation Error: {e}")
    else:
        st.error("No text found to translate.")
