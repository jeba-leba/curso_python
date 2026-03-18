# Esta é uma maneira de definir listas

idades = [30, 28, 46, 31, 29, 22]
print(idades)

jebaleba = ["Jean", "Benjamim", 30, 0, "Casado", 2500]
print(jebaleba)

# Acessando elementos dentro da lista

#nome
print(jebaleba[0])

#sobrenome
print(jebaleba[1])

#idade
print(jebaleba[2])

# Soma e divisão de todas as idades

print("Soma das idades: ",sum(idades))

print("Qtde de idades:", len(idades))

print("Média idades: ", sum(idades)/len(idades))

# Elemento mín e máx

print("Menor idade:", min(idades))

print("Maior idade:", max(idades))

# lista dentro de lista

dados = ["Jean Benjamim", 30, "desempregado", 
        ["Cynthia Magalhães", 29, "Servidora"],
        ["Mateus Ferreira", 25, "Programador CNC"]]

# Puxando o nome da Cynthia na lista dados
print(dados[3][0])

# Puxando a ultima lista.

tamanho = len(dados)
ultima_lista = tamanho -1
mateus = dados[ultima_lista]
print(dados[ultima_lista])

# Puxando cargo Mateus

print(dados[ultima_lista][len(mateus) -1])

# Outra forma de puxar a ultima lista com apenas -1

print(dados[-1])

# Outra forma de puxar o cargo do Mateus que é o
# ultimo elemento da ultima lista

print(dados[-1][-1])