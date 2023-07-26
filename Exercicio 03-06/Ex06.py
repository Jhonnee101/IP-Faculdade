salario = float(input("Digite o seu salario atual: R$ "))
inss = salario - (salario * 0.08)
if salario > 2300:
    impostoRenda = inss - (inss * 0.05)
    print(f"Seu salario se enquadra no desconto do Imposto de renda, seu salario liquido vai ficar R${impostoRenda}")
else:
    print(f"Seu salario liquido ficou R${inss} com o desconto do INSS.")