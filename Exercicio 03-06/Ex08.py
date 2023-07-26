fixo = 800.00
vendas = int(input("Digite a quantidade de vendas deste mes: "))
comissao = (fixo * 0.25) * vendas
salarioliquido = comissao + fixo
print(f"Este mes voce vendeu {vendas} produtos, seu salario liquido ficou R${salarioliquido}")