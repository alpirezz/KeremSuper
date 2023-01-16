import streamlit as st

st.title("Kerem bu hafta Weekly'de 'Süper...' dedi mi?")
answer = st.radio("Seçiniz:", ("Dedi", "Demedi"))

if answer == "Dedi":
    st.success("Doğru cevap! Kerem bu hafta Weekly'de 'Süper...' dedi.")
    st.image("success.jpg") # path to your image file
else:
    st.error("Yanlış cevap! Kerem bu hafta Weekly'de 'Süper...' demedi.")
    st.image("incorrect.jpg") # path to your image file
