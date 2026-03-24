import requests # Para realizar requisições HTTP
import json # Para tratar json de listas/dicionarios para arquivos
from tqdm import tqdm # Mostra a barra de progresso da iteração

import pandas as pd # Para criar o dataset e exportar para csv

# CEPS para consulta
ceps = [
    "72405135",
    "14031140",
    "14026230",
    "14035100",
    "14120200",
    "14020150",
]

url = "https://viacep.com.br/ws/{ceps}/json/"
dados = []


for i in tqdm(ceps):
    resposta = requests.get(url.format(ceps=i))
    if resposta.status_code == 200:
        dados.append(resposta.json())

dados

dataset = pd.DataFrame(dados)
dataset.to_csv("cep.csv", sep=";")

with open("cep.json", "w", encoding='utf-8') as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4)

