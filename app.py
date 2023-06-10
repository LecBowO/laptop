import streamlit as st
import pickle
import sklearn
import pandas as pd

df = pickle.load(open('df.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.set_page_config(page_icon='favicon.ico', page_title='LAPTOP | PRICE | PREDICTOR')

st.title("Laptop Price Pridictor")

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col5, col6 = st.columns(2)
col7, col8 = st.columns(2)
col9, col10 = st.columns(2)
col11, col12 = st.columns(2)


with col1:
    company = st.selectbox("Select The Company", df['Company'].unique())
with col2:
    laptop_type = st.selectbox("Select Laptop Type", df['TypeName'].unique())
with col3:
    ram = st.selectbox("Select Laptop Ram", df['Ram'].sort_values(ascending=True).unique())
with col4:
    weight = st.number_input("Enter Laptop Weight")
with col5:
    touch_screen = st.selectbox("Touch Screen", ("Yes", 'No'))
with col6:
    ips = st.selectbox("IPS Screen", ("Yes", 'No'))
with col7:
    ppi = st.number_input("Enter PPI")
with col8:
    hdd = st.selectbox("Select HDD", df['HDD'].unique())
with col9:
    ssd = st.selectbox("Select SSD", df['SSD'].sort_values().unique())
with col10:
    gpu = st.selectbox("GPU Brand", df['Gpu_brand'].unique())
with col11:
    op = st.selectbox("Oprating System", df['Op'].unique())
with col12:
    cpu = st.selectbox("CPU Brand", df['Cpu_brand'].unique())

if st.button("Predict"):
    if touch_screen == 'No':
        touch_screen = 0
    else:
        touch_screen = 1

    if ips == "Yes":
        ips = 1
    else:
        ips = 0
    input_data = [[company, laptop_type, ram, weight, touch_screen, ips, ppi, hdd, ssd, gpu, op, cpu]]
    prediction = model.predict(input_data)
    prediction = prediction[0]
    prediction = int(prediction)
    st.subheader(prediction)
