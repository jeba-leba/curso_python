def calc_imposto(preco:float, tx_base:float, **kwargs):
    imposto = preco * tx_base

    for i in kwargs:
        print(i, kwargs[i])
        imposto += preco * kwargs[i]

    return imposto

preco = float(input("Insira o valor do produto: "))
tx_base = float(input("Insira a taxa base de imposto em porcentagem: ")) / 100

impostos_gerais = {
    "municipal": 0.01,
    "estadual": 0.02,
    "federal": 0.05
}
print(calc_imposto(preco, tx_base, **impostos_gerais))



