import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

#Datas

hsPlot = pd.read_csv('Visualization/hsPlot.csv', index_col=[0])
hsPlotD = pd.read_csv('Visualization/hsPlotD.csv', index_col=[0])

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def hsDbar(colName):

    plotBarh = hsPlotD.copy()

    if colName == 'Bulan':
        plotBarh['Bulan'] = pd.Categorical(plotBarh['Bulan'], categories=months, ordered=True)

    plotBarh = plotBarh.sort_values(by=colName)
    fig = plt.figure(figsize=(10, 5))
    sns.countplot(y = colName, data = plotBarh)

    st.pyplot(fig)
    
def hsMVis1():

    bbox = (94.241, 108.809, -6.404, 6.513)
    mapbg = plt.imread('Visualization/map.png')
    fig, ax = plt.subplots(figsize = (8,7))
    ax.scatter(hsPlot.Longitude, hsPlot.Latitude, zorder=1, alpha= 0.2, c='b', s=10)
    ax.set_title('Lokasi Kebakaran Hutan dan Lahan')
    ax.set_xlim(bbox[0],bbox[1])
    ax.set_ylim(bbox[2],bbox[3])
    ax.imshow(mapbg, zorder=0, extent = bbox, aspect= 'equal')

    st.pyplot(fig)

def hsMVis2(month, year):

    plotMVis = hsPlotD.copy()
    cond_ = (hsPlotD['Bulan'].isin([month])) & (hsPlotD['Tahun'] == int(year))
    plotMVis = plotMVis.loc[cond_,:]

    if (plotMVis.shape[0] == 0):
        st.code('Tidak ada data pada bulan tersebut')
    else:
        bbox = (94.241, 108.809, -6.404, 6.513)
        mapbg = plt.imread('map.png')
        fig, ax = plt.subplots(figsize = (8,7))
        ax.scatter(plotMVis.Longitude, plotMVis.Latitude, zorder=1, alpha= 0.2, c='b', s=10)
        ax.set_title('Lokasi Kebakaran Hutan dan Lahan', )
        ax.set_xlim(bbox[0],bbox[1])
        ax.set_ylim(bbox[2],bbox[3])
        ax.imshow(mapbg, zorder=0, extent = bbox, aspect= 'equal')

        st.pyplot(fig)

def hsHist(colName):
    fig, ax = plt.subplots()
    ax.hist(hsPlot[colName])

    st.pyplot(fig)

st.set_page_config(page_title="Visualisasi Data")

st.header('Visualisasi Data Kebakaran Hutan dan Lahan terhadap kondisi Cuaca')

st.subheader('Informasi Data Kebakaran dan Cuaca')
st.code( '''
    hotSpot.info()

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 54903 entries, 0 to 54902
    Data columns (total 12 columns):
    #   Column      Non-Null Count  Dtype
    ---  ------      --------------  -----
    0   Unnamed: 0  54903 non-null  int64
    1   Provinsi    54903 non-null  object
    2   Kab Kota    54903 non-null  object
    3   Kecamatan   54728 non-null  object
    4   Desa        54710 non-null  object
    5   Tanggal     54903 non-null  object
    6   Waktu       54903 non-null  object
    7   Latitude    54903 non-null  float64
    8   Longitude   54903 non-null  float64
    9   WD10M       54903 non-null  float64
    10  WD2M        54903 non-null  float64
    11  T2M         54903 non-null  float64
    dtypes: float64(5), int64(1), object(6)
    memory usage: 5.0+ MB
    ''')


st.markdown('###')
st.subheader('Hubungan Kebakaran dengan Tanggal Kejadian')

st.markdown('#####')
st.markdown('**Horizontal Bar Plot untuk jumlah kebakaran terhadap waktu kejadian**')
sortByT1 = st.selectbox('Jumlah kebakaran berdasarkan:', ['Hari', 'Bulan', 'Tahun'], key = 'sortByT1')

if st.button('Generate Plot', key = 'hsDbar'):
    hsDbar(sortByT1)
else:
    st.code('Tekan tombol untuk menampilkan plot')

st.markdown('####')
st.markdown('**Visualisasi lokasi kebakaran pada peta pulau Sumatera (2016-2020)**')

hsMVis1()

st.markdown('####')
st.markdown('**Visualisasi lokasi kebakaran pada peta pulau Sumatera pada bulan & tahun tertentu**')
sortByT2 = st.selectbox('Bulan: ', ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], key = 'sortByT2')
sortByT3 = st.selectbox('Tahun: ', ['2016', '2017', '2018', '2019', '2020'], key = 'sortByT3')

if st.button('Generate Plot', key = 'hsMVis2'):
    hsMVis2(sortByT2, sortByT3)
else:
    st.code('Tekan tombol untuk menampilkan plot (Data tersedia April 2016 - Desember 2020)')