import requests
import pandas as pd

url = "https://api.open-meteo.com/v1/forecast?latitude=-8.05&longitude=-34.88&hourly=temperature_2m&timezone=America/Sao_Paulo"

resposta = requests.get(url)

dados = resposta.json()

listas_datas = dados["hourly"]["time"]
listas_temperatura = dados["hourly"]["temperature_2m"]

dicionario_tabela = {
    "Data_e_Hora": listas_datas,
    "Temperatura_C": listas_temperatura
}

df = pd.DataFrame(dicionario_tabela)
df.to_csv("previsão_tempo_recife.csv", index=False)
print("Tabela de previsão do tempo gerada com sucesso!")
print(listas_datas)

print(listas_temperatura)
