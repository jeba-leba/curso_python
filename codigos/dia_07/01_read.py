
nome_arquivo = "historia.txt"

# Abre o arquivo.
open_file = open(nome_arquivo)

# Lê o conteúdo do arquivo.
conteudo = open_file.read()
print(conteudo)

# Fecha o arquivo.
open_file.close()

# O que está acima é passivel de você esquecer de fechar o arquivo

# O jeito mais recomendado é usar o with, que fecha o arquivo automaticamente
with open(nome_arquivo) as open_file:
    conteudo = open_file.read()
    print(conteudo)