import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt

import plotly.figure_factory as ff

st.set_page_config(
    page_title="Visualisasi Data Arah Angin",
)

hsPlot = pd.read_csv('Visualization/hsPlot.csv', index_col=[0])
hsPlotQ = pd.read_csv('Visualization/hsPlotQ.csv', index_col=[0])

def hsHist(colName):
    fig, ax = plt.subplots()
    ax.hist(hsPlot[colName])

    st.pyplot(fig)

def hsMVisWD(month, year):
    plotMVis = hsPlotQ.copy()
    cond_ = (hsPlotQ['Bulan'].isin([month])) & (hsPlotQ['Tahun'] == int(year))
    plotMVis = plotMVis.loc[cond_,:]

    if (plotMVis.shape[0] == 0):
        st.code('Tidak ada data pada bulan tersebut')
    else:
        fig = ff.create_quiver(plotMVis.Longitude, plotMVis.Latitude, plotMVis.U, plotMVis.V)
        st.plotly_chart(fig)

st.header('Visualisasi Data Arah Angin')

st.subheader('Hubungan Kebakaran dengan Arah Angin')

st.markdown('#####')
st.markdown('**Histogram untuk jumlah kebakaran terhadap arah angin**')
st.caption('Jumlah kebakaran terhadap arah angin (WD2M)')
hsHist('WD2M')
st.caption('Jumlah kebakaran terhadap arah angin (WD10M)')
hsHist('WD10M')

st.markdown('####')
st.markdown('**Visualisasi lokasi kebakaran pada peta pulau Sumatera (arah angin, per bulan)**')
sortByT4 = st.selectbox('Bulan: ', ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], key = 'sortByT4')
sortByT5 = st.selectbox('Tahun: ', ['2016', '2017', '2018', '2019', '2020'], key = 'sortByT5')

if st.button('Generate Plot', key = 'hsMVisWD'):
    hsMVisWD(sortByT4, sortByT5)
else:
    st.code('Tekan tombol untuk menampilkan plot (Data tersedia April 2016 - Desember 2020)')

st.caption('Zoom in pada plot menggunakan button yang tersedia di kanan atas plot untuk melihat panah arah angin dengan lebih jelas')
