import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Visualisasi Model",
)

xTrain = pd.read_csv('Visualization/xTrain.csv', index_col=[0])
yTrain = pd.read_csv('Visualization/yTrain.csv', index_col=[0])
xTest = pd.read_csv('Visualization/xTest.csv', index_col=[0])
yTest = pd.read_csv('Visualization/yTest.csv', index_col=[0])
mlrpred = pd.read_csv('Visualization/mlrpred1.csv', index_col=[0])
rfpred = pd.read_csv('Visualization/rfpred1.csv', index_col=[0])
svmpred = pd.read_csv('Visualization/svmpred1.csv', index_col=[0])

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

def hsMVisP(model):

    bbox = (94.241, 108.809, -6.404, 6.513)
    mapbg = plt.imread('Visualization/map.png')
    fig, ax = plt.subplots(figsize = (8,7))
    ax.scatter(model.Longitude, model.Latitude, zorder=1, alpha= 0.2, c='b', s=10)
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

st.subheader('Random Forest')
hsMVisP(rfpred)

evalRF = pd.DataFrame.from_dict({
        'Model': ['Random Forest'], 
        'MSE': [3.21], 
        'RMSE': [1.78], 
        'MAE': [1.22]
}).set_index('Model')
st.table(evalRF)

st.subheader('Multinomial Logistic Regression')
hsMVisP(mlrpred)

evalMLR = pd.DataFrame.from_dict({
        'Model': ['Multinomial Logistic Regression'], 
        'MSE': [8.38], 
        'RMSE': [2.89], 
        'MAE': [2.32]
}).set_index('Model')
st.table(evalMLR)

st.subheader('Support Vector Machine')
hsMVisP(svmpred)

evalSVM = pd.DataFrame.from_dict({
        'Model': ['Support Vector Machine'], 
        'MSE': [6.31], 
        'RMSE': [2.50], 
        'MAE': [2.05]
}).set_index('Model')
st.table(evalSVM)
