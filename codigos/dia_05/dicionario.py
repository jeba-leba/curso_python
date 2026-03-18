dados_jeba = {"nome":"Jeba",
               "filhos":False,
               "sobrenome":"Benjamim",
               "formacao":["Gestão de Produção", "Pós em Lean Six Sigma"],
               "cargos":[
                   {"nome":"Auxiliar Qualidade","empresa":"Três-S"},
                   {"nome":"Coordenador Qualidade","empresa":"Três-S"},
                   ]
                }

print(dados_jeba["nome"])
print(dados_jeba["sobrenome"])
print(dados_jeba["formacao"][-1])
print(dados_jeba["cargos"][-1]["empresa"])


dados_jeba["estado civil"] = "casado"
print(dados_jeba)

print(f"Chaves:", dados_jeba.keys())
print(f"Valores:", dados_jeba.values())
print(f"Chaves e Valores:", dados_jeba.items())



for i in dados_jeba:
    print(i, "-", dados_jeba[i])


for chave, valor in dados_jeba.items():
    print(chave, "-", valor)

