import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado principal
st.header("Análisis de Anuncios de Venta de Coches")
st.write("Explora el dataset de vehículos usados en EE.UU.")

# --- Histograma ---
st.subheader("Distribución del Odómetro")
hist_check = st.checkbox("Mostrar histograma del odómetro")

if hist_check:
    st.write("Histograma que muestra la distribución del kilometraje de los vehículos")
    fig = px.histogram(car_data, x="odometer", title="Distribución del Odómetro")
    st.plotly_chart(fig, use_container_width=True)

# --- Gráfico de dispersión ---
st.subheader("Relación entre Precio y Odómetro")
scatter_check = st.checkbox("Mostrar gráfico de dispersión")

if scatter_check:
    st.write("Relación entre el precio del vehículo y su kilometraje")
    fig2 = px.scatter(car_data, x="odometer", y="price", title="Precio vs Odómetro")
    st.plotly_chart(fig2, use_container_width=True)