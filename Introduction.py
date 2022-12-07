import streamlit as st

st.set_page_config(
    page_title="Introduction",
)

st.header("Kebakaran Hutan dan Lahan di Pulau Sumatera berdasarkan kondisi Cuaca")

st.markdown(
    '''
    Penelitian ini bertujuan untuk melakukan identifikasi terhadap kemungkinan penyebaran kebakaran hutan dan lahan 
    berdasarkan kondisi cuaca di daerah pulau Sumatera dengan menggunakan pendekatan Multinomial Logistic Regression,
    Random Forest dan Support Vector Machine.

    Daftar isi
    1. Visualisasi Data Kebakaran Hutan dan Lahan 
    2. Visualisasi Data terhadap Arah Angin
    3. Visualisasi Data terhadap Temperatur
    2. Visualisasi Hasil Prediksi Model
    '''
)

st.sidebar.success("Pilih halaman")