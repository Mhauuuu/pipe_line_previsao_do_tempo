import streamlit as st
import pandas as pd

st.title("Previsão do tempo - Recife e Olinda")
st.write("Acompanhe a variação de temperatura para os proximos dias")

df = pd.read_csv("previsão_tempo_recife.csv")
st.line_chart(data=df, x="Data_e_Hora", y="Temperatura_C")

st.subheader("Tabela de Dados")
st.dataframe(df)