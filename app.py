import streamlit as st
import pandas as pd
import plotly.express as px

#Cabeçalho
st.header("Dashboard de Veículos")

#Ler os dados
df = pd.read_csv('vehicles.csv')

#Botão do histograma
if st.button("Criar histograma"):
    st.write("Histograma da quilometragem dos veículos")
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig, width=True)

#Botão do gráfico de dispersão
if st.button("Criar gráfico de dispersão"):
    st.write("Relação entre preço e quilometragem")
    fig = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig, width=True)