import streamlit as st
import pandas as pd
import sqlite3


st.title("⛅ Previsão do Tempo - Recife e Olinda")
st.write("Acompanhe a variação de temperatura para os próximos dias.")


conexao = sqlite3.connect("banco_clima.db")

query_metricas = "SELECT MAX(Temperatura_C) as max_temp, MIN(Temperatura_C) as min_temp FROM previsao"
df_metricas = pd.read_sql(query_metricas, con=conexao)


temp_maxima = df_metricas["max_temp"][0]
temp_minima = df_metricas["min_temp"][0]


col1, col2 = st.columns(2)
col1.metric(label="Temperatura Máxima 📈", value=f"{temp_maxima} °C")
col2.metric(label="Temperatura Mínima 📉", value=f"{temp_minima} °C")

st.divider() 

df_grafico = pd.read_sql("SELECT * FROM previsao", con=conexao)
conexao.close() 

st.line_chart(data=df_grafico, x="Data_e_Hora", y="Temperatura_C")

st.subheader("Tabela de Dados")
st.dataframe(df_grafico)