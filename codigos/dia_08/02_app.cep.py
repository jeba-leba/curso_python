import streamlit as st
import requests
import pandas as pd

url = "https://viacep.com.br/ws/{cep}/json/"

st.title("Busca CEP")

cep = st.text_input("Entre com o CEP para consulta")

if cep != "":
    try:
        resp = requests.get(url.format(cep=cep))
        data = pd.DataFrame([resp.json()])

        st.dataframe(data, hide_index=True)

    except Exception as err:
        st.error("Erro ao consultar CEP. O CEP digitado é invalido ou não existe.")