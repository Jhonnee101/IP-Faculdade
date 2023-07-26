from funcoes import soma,multiplicacao,divisao,subtracao

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
print('''Escolha a operacao que deseja
      [1]- Adicao
      [2]- Subtracao    
      [3]- Multiplicacao
      [4]- Divisao''')
opcao = int(input('Digite a sua opçao: '))
if opcao == 1:
    valor = soma(n1,n2)
    print(f'{n1} + {n2} = {valor}')
elif opcao == 2:
    valor = subtracao(n1,n2)
    print(f'{n1} - {n2} = {valor}')
elif opcao == 3:
    valor = multiplicacao(n1,n2)
    print(f'{n1} x {n2} = {valor}')
elif opcao == 4:
    valor = divisao(n1,n2)
    print(f'{n1} / {n2} = {valor}')
else:
    print('Invalido')