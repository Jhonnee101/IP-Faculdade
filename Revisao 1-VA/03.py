def sumrange(x,y):
    soma = 0
    for i in range(x,(y+1)):
        soma += i
        print(soma)
    return soma
    
def main():
    x1 = int(input('Digite o primeiro numero '))
    y1 = int(input('Digite o segundo numero '))
    chamar = sumrange(x1,y1)

main()