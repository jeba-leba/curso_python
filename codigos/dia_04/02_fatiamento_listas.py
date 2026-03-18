# Pegar vários elementos de uma lista

dados = ["Jean Benjamim", 30, "desempregado", 
        ["Cynthia Magalhães", 29, "Servidora"],
        ["Mateus Ferreira", 25, "Programador CNC"]]

print(dados[0:3])
print(dados[:3])

# Como pegar a idade e a profissão da Cynthia

print(dados[3][1:3])
print(dados[3][-2:])

# Se eu quiser começar do começo da lista ou ir até o final
# Não preciso especificar o começo e o fim

# Para trázer a lista de trás pra frente

print(dados[::-1])

# Para ir pulando na lista com start : stop : step

print(dados[::2])