import streamlit as st

st.title("Kerem bu hafta Weekly'de 'Süper...' dedi mi?")
answer = st.radio("Seçiniz:", ("Dedi", "Demedi"))

if answer == "Demedi":
    st.success("Doğru cevap! Kerem bu hafta Weekly'de 'Süper...' demedi.")
    st.image("success.jpg")
else:
    st.error("Yanlış cevap! Kerem bu hafta Weekly'de 'Süper...' demedi.")
    st.image("incorrect.jpg")
