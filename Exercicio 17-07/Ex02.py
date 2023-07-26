def pagamento(opcao):
    if opcao == 1:
        desconto = (gasto*0.1)-gasto
        return desconto
    elif opcao == 2:
        return gasto
    elif opcao == 3:
        aumento = (parcelas * 0.03)*(gasto) + gasto
        return aumento
gasto = float(input('Digite o valor dos produtos: '))
print('''Escolha a forma de pagamento
      [1]- A vista com 10% de desconto
      [2]- Parcelado em 2 vezes(Sem desconto)
      [3]- 3 a 10 vezes com 3% de juros ao mes''')
opcao = int(input('Digite a sua opçao: '))
if opcao == 3 and gasto >= 100:
    parcelas = int(input('Em quantas parcelas voce ira dividir: '))
else:
    print('Valor minimo para parcelamento menor que R$100.00') 
print(f'Sua compras ficaram no valor de R${gasto}, e sua forma de pagamento foi {opcao}, o valor final de pagamento ficou R$',pagamento(opcao))


