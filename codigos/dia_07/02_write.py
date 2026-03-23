
nome_arquivo = "historia_02.txt"

txt = "Se eu quiser pular uma linha, basta eu usar o '\\n' no meu texto \n"


with open(nome_arquivo, "a") as open_file:
    open_file.write(txt)