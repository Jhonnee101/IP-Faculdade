print('='*22)
print('[1] Para somar')
print('[2] Para subtrair')
print('[3] Para multiplicar')
print('[4] Para dividir')
print('='*22)
escolha = int(input('Faça a sua escolha: '))
n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
if escolha == 1:
    soma = n1+n2
    print(f'{n1} + {n2} = {soma}')
elif escolha == 2:
    sub = n1-n2
    print(f'{n1} - {n2} = {sub}')
elif escolha == 3:
    multi = n1*n2
    print(f'{n1} x {n2} = {multi}')
elif escolha == 4:
    div = n1+n2
    print(f'{n1} / {n2} = {div}')
else:
    print('Opção Invalida')
