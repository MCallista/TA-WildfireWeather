import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt

import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Visualisasi Data Temperatur"
)

hsPlot = pd.read_csv('Visualization/hsPlot.csv', index_col=[0])
hsPlotD = pd.read_csv('Visualization/hsPlotD.csv', index_col=[0])

hsPlotT = hsPlot.copy()
hsPlotT = hsPlotT.sort_values(by='Tanggal')
hsPlotT = hsPlotT.reset_index(drop=True)
hsPlotT['Tanggal'] = pd.to_datetime(hsPlotT['Tanggal'], format = '%Y-%m-%d')
hsPlotT['Tanggal'] = hsPlotT['Tanggal'].dt.strftime('%Y-%m-%d')

def hsHist(colName):
    fig, ax = plt.subplots()
    ax.hist(hsPlot[colName])

    st.pyplot(fig)

def hsMVisT1():
    bbox = (94.241, 108.809, -6.404, 6.513)
    mapbg = plt.imread('Visualization/map.png')
    fig, ax = plt.subplots(figsize = (8,7))
    sc = ax.scatter(hsPlot.Longitude, hsPlot.Latitude, zorder=1, alpha= 0.2, c=hsPlot.T2M, cmap='jet', s=10)
    ax.set_title('Lokasi Kebakaran Hutan dan Lahan', )
    ax.set_xlim(bbox[0],bbox[1])
    ax.set_ylim(bbox[2],bbox[3])
    fig.colorbar(sc, ax=ax)
    ax.imshow(mapbg, zorder=0, extent = bbox, aspect= 'equal')

    st.pyplot(fig)

def hsMVisT2(month, year):
    plotMVis = hsPlotD.copy()
    cond_ = (hsPlotD['Bulan'].isin([month])) & (hsPlotD['Tahun'] == int(year))
    plotMVis = plotMVis.loc[cond_,:]

    if (plotMVis.shape[0] == 0):
        st.code('Tidak ada data pada bulan tersebut')
    else:
        bbox = (94.241, 108.809, -6.404, 6.513)
        mapbg = plt.imread('Visualization/map.png')
        fig, ax = plt.subplots(figsize = (8,7))
        sc = ax.scatter(plotMVis.Longitude, plotMVis.Latitude, zorder=1, alpha= 0.2, c=plotMVis.T2M, cmap='jet', s=10)
        ax.set_title('Lokasi Kebakaran Hutan dan Lahan', )
        ax.set_xlim(bbox[0],bbox[1])
        ax.set_ylim(bbox[2],bbox[3])
        fig.colorbar(sc, ax=ax)
        ax.imshow(mapbg, zorder=0, extent = bbox, aspect= 'equal')

        st.pyplot(fig)

st.header('Visualisasi Data Temperatur')

st.subheader('Hubungan Kebakaran dengan Temperatur')

st.markdown('#####')
st.markdown('**Histogram untuk jumlah kebakaran terhadap temperatur**')
hsHist('T2M')

st.markdown('####')
st.markdown('**Visualisasi lokasi kebakaran pada peta pulau Sumatera (temperatur)**')
hsMVisT1()

st.markdown('####')
st.markdown('**Visualisasi lokasi kebakaran pada peta pulau Sumatera (temperatur, per bulan)**')
sortByT6 = st.selectbox('Bulan: ', ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], key = 'sortByT6')
sortByT7 = st.selectbox('Tahun: ', ['2016', '2017', '2018', '2019', '2020'], key = 'sortByT7')

if st.button('Generate Plot', key = 'hsMVisT'):
    hsMVisT2(sortByT6, sortByT7)
else:
    st.code('Tekan tombol untuk menampilkan plot (Data tersedia April 2016 - Desember 2020)')

st.markdown('####')
st.markdown('**Visualisasi lokasi kebakaran pada peta pulau Sumatera (temperatur, per hari)**')

hsMVisT3 = px.scatter_geo(hsPlotT, lat = "Latitude", lon = "Longitude", color = "T2M", animation_frame = "Tanggal", opacity = 0.2)
hsMVisT3.add_traces(go.Scattergeo(lat=[-6,6], lon=[94,108], mode = 'markers', marker = dict(size = 2,color = 'rgba(0, 0, 0, 0)'), name='Sumatera'))
hsMVisT3.update_geos(visible=True, resolution=50, scope="asia", fitbounds='locations', showcountries=True, countrycolor="Black", showsubunits=True, subunitcolor="grey")

st.plotly_chart(hsMVisT3)
