import streamlit as st
import requests

url = "http://127.0.0.1:8000/kave"

st.title("SumAPI Duygu Analizi Uygulaması")

user_input = st.text_input("Bir şeyler yazın:")

if user_input:
    response = requests.get(f'{url}/{user_input}')
    if response.status_code == 200:
        data = response.json()
        result_data = data.get('result', {})
        sentiment = result_data.get('sentiment')
        color = result_data.get('color')
        st.write(
            f'<div style="color: {color};">Duygu Analizi Sonucu: {sentiment}</div>', unsafe_allow_html=True)
    else:
        st.write("Error at backend")
