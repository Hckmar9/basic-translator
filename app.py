import streamlit as st
from googletrans import Translator, LANGUAGES

translator = Translator()
st.title("Text Translator")

input_text = st.text_area("Add the text you want to translate:")
languages = list(LANGUAGES.values())
src_language = st.selectbox("Select main language:", languages, index=languages.index("english"))
dest_language = st.selectbox("Select desired language:", languages, index=languages.index("spanish"))

if st.button("Translate"):
    if input_text:
        src_code = [code for code, lang in LANGUAGES.items() if lang == src_language][0]
        dest_code = [code for code, lang in LANGUAGES.items() if lang == dest_language][0]
        
        translation = translator.translate(input_text, src=src_code, dest=dest_code)
        st.subheader("Translated Text:")
        st.write(translation.text)
    else:
        st.error("Add some text to translate.")