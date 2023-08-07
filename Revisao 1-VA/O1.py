salario = 800
cont = 0

while cont < 100:
    vendas = int(input('Digite a quantidade de vendas: '))
    aumento = vendas * 0.25
    novosalario = salario + (salario * aumento)
    print(novosalario)
    cont += 1
    
    