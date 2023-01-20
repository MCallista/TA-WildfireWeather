import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Visualisasi Data Training",
)

xTrain = pd.read_csv('Visualization/xTrain.csv', index_col=[0])
yTrain = pd.read_csv('Visualization/yTrain.csv', index_col=[0])
xTest = pd.read_csv('Visualization/xTest.csv', index_col=[0])
yTest = pd.read_csv('Visualization/yTest.csv', index_col=[0])

yhTrain = pd.read_csv('Visualization/yhTrain.csv', index_col=[0])
yhTest = pd.read_csv('Visualization/yhTest.csv', index_col=[0])

def hsMVisPR():

    bbox = (94.241, 108.809, -6.404, 6.513)
    mapbg = plt.imread('Visualization/map.png')
    fig, ax = plt.subplots(figsize = (8,7))
    ax.scatter(yTest.Longitude, yTest.Latitude, zorder=1, alpha= 0.2, c='b', s=10)
    ax.set_title('Prediksi Lokasi Kebakaran Hutan dan Lahan')
    ax.set_xlim(bbox[0],bbox[1])
    ax.set_ylim(bbox[2],bbox[3])
    ax.imshow(mapbg, zorder=0, extent = bbox, aspect= 'equal')

    st.pyplot(fig)

st.header("Visualisasi Prediksi Model")

st.subheader('Data Training')
st.markdown('**Tampilan fitur data (xTrain) yang digunakan untuk training**')
st.dataframe(xTrain)

st.markdown('**Tampilan hasil data (yTrain) yang digunakan untuk training**')
st.dataframe(yTrain)

st.markdown('**Tampilan fitur data (xTest) yang digunakan untuk testing**')
st.dataframe(xTest)

st.markdown('**Tampilan hasil data (yTest) yang digunakan untuk testing**')
st.dataframe(yTest)

st.markdown('**Visualisasi hasil data (yTest) yang digunakan untuk testing**')
hsMVisPR()

st.markdown('**Tampilan hasil data (yhTrain) yang digunakan untuk training (dengan implementasi geohash)**')
st.dataframe(yhTrain)

st.markdown('**Tampilan hasil data (yhTest) yang digunakan untuk testing (dengan implementasi geohash)**')
st.dataframe(yhTest)
