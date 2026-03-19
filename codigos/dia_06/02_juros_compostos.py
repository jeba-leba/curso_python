def juros_compostos(aporte:float, taxa:float, anos:int)->float:
    """
    juros_compostos serve para calcular o retorno financeiro a partir de um aporte inicial
    deve-se considerar um valor, a taxa de juros atual e o tempo em anos de investimento,
    para o calculo do valor final.

    aporte:
        um valor float que representa o valor inicial investido
    taxa:
        um valor float que representa a taxa de juros anual em porcentagem
    anos: 
        um valor inteiro que representa o tempo em anos do investimento
    """

    return aporte * (1 + taxa) ** anos

aporte = float(input("Qual o seu aporte inicial? "))
taxa = float(input("Qual a taxa de juros anual? ")) / 100
anos = int(input("Quantos anos deseja investir? "))

print(f" Seu Saldo em {anos} anos é de R$ {juros_compostos(aporte, taxa, anos):.2f}")
