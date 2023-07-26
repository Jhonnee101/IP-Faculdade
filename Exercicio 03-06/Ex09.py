revendedor = 0.25
impostos = 0.45
custo = float(input("Digite o custo de fabrica para montar o automovel:R$ "))
imposto = (custo * impostos) + custo
valorfinal = (imposto * revendedor) + imposto
print(f"Para o consumidor final o preço do automovel será de R${valorfinal}") 