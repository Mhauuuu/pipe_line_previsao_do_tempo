import streamlit as st
import pandas as pd
import sqlite3

st.title("Previsão do tempo - Recife e Olinda")
st.write("Acompanhe a variação de temperatura para os proximos dias")

conexao = sqlite3.connect("banco_clima.db")
df = pd.read_sql("SELECT * FROM previsao", con=conexao)
conexao.close()

st.line_chart(data=df, x="Data_e_Hora", y="Temperatura_C")

st.subheader("Tabela de Dados")
st.dataframe(df)

