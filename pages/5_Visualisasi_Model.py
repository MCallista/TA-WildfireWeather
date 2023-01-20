import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Visualisasi Model",
)

mlrpred = pd.read_csv('Visualization/mlrpred1.csv', index_col=[0])
rfpredr = pd.read_csv('Visualization/rfpred1.csv', index_col=[0])
rfpredc = pd.read_csv('Visualization/rfpred2.csv', index_col=[0])
svmpredr = pd.read_csv('Visualization/svmpred1.csv', index_col=[0])
svmpredc = pd.read_csv('Visualization/svmpred3.csv', index_col=[0])

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

st.subheader('Multinomial Logistic Regression (MLR)')
st.markdown('**Model Klasifikasi dengan nilai koordinat dalam bentuk Geohash**')
hsMVisP(mlrpred)

evalMLR = pd.DataFrame.from_dict({
        'Model': ['Multinomial Logistic Regression'], 
        'MSE': [8.3679], 
        'RMSE': [2.8927], 
        'MAE': [2.3239]
}).set_index('Model')
st.table(evalMLR)

st.markdown('**Visualisasi prediksi kebakaran (MLR, per hari)**')

hsMVisMLR = px.scatter_geo(mlrpred, lat = "Latitude", lon = "Longitude", animation_frame = "Tanggal", opacity = 0.2)
hsMVisMLR.add_traces(go.Scattergeo(lat=[-6,6], lon=[94,108], mode = 'markers', marker = dict(size = 2,color = 'rgba(0, 0, 0, 0)'), name='Sumatera'))
hsMVisMLR.update_geos(visible=True, resolution=50, scope="asia", fitbounds='locations', showcountries=True, countrycolor="Black", showsubunits=True, subunitcolor="grey")

st.plotly_chart(hsMVisMLR)

st.subheader('Random Forest (RF)')
st.markdown('**Model Regresi dengan nilai koordinat terpisah (RF1)**')
hsMVisP(rfpredr)

evalRFr = pd.DataFrame.from_dict({
        'Model': ['Random Forest 1'], 
        'MSE': [3.2131], 
        'RMSE': [1.7767], 
        'MAE': [1.2208]
}).set_index('Model')
st.table(evalRFr)

st.markdown('**Model Klasifikasi dengan nilai koordinat dalam bentuk Geohash (RF2)**')
hsMVisP(rfpredc)

evalRFc = pd.DataFrame.from_dict({
        'Model': ['Random Forest 2'], 
        'MSE': [6.5378], 
        'RMSE': [2.5497], 
        'MAE': [1.7698]
}).set_index('Model')
st.table(evalRFc)

st.markdown('**Visualisasi prediksi kebakaran (RF2, per hari)**')

hsMVisRF = px.scatter_geo(rfpredc, lat = "Latitude", lon = "Longitude", animation_frame = "Tanggal", opacity = 0.2)
hsMVisRF.add_traces(go.Scattergeo(lat=[-6,6], lon=[94,108], mode = 'markers', marker = dict(size = 2,color = 'rgba(0, 0, 0, 0)'), name='Sumatera'))
hsMVisRF.update_geos(visible=True, resolution=50, scope="asia", fitbounds='locations', showcountries=True, countrycolor="Black", showsubunits=True, subunitcolor="grey")

st.plotly_chart(hsMVisRF)

st.subheader('Support Vector Machine (SVM)')
st.markdown('**Model Regresi dengan nilai koordinat terpisah (SVM1)*')
hsMVisP(svmpredr)

evalSVMr = pd.DataFrame.from_dict({
        'Model': ['Support Vector Machine'], 
        'MSE': [6.3079], 
        'RMSE': [2.5012], 
        'MAE': [2.0521]
}).set_index('Model')
st.table(evalSVMr)

st.markdown('**Model Klasifikasi dengan nilai koordinat dalam bentuk Geohash (SVM2)**')
hsMVisP(svmpredc)

evalSVMc = pd.DataFrame.from_dict({
        'Model': ['Support Vector Machine'], 
        'MSE': [12.3327], 
        'RMSE': [3.5074], 
        'MAE': [2.6635]
}).set_index('Model')
st.table(evalSVMc)

st.markdown('**Visualisasi prediksi kebakaran (SVM2, per hari)**')

hsMVisSVM = px.scatter_geo(svmpredc, lat = "Latitude", lon = "Longitude", animation_frame = "Tanggal", opacity = 0.2)
hsMVisSVM.add_traces(go.Scattergeo(lat=[-6,6], lon=[94,108], mode = 'markers', marker = dict(size = 2,color = 'rgba(0, 0, 0, 0)'), name='Sumatera'))
hsMVisSVM.update_geos(visible=True, resolution=50, scope="asia", fitbounds='locations', showcountries=True, countrycolor="Black", showsubunits=True, subunitcolor="grey")

st.plotly_chart(hsMVisSVM)
