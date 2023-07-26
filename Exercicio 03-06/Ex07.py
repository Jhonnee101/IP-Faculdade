nome = str(input("Digite o seu nome: "))
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso / (altura * altura)
if imc > 25.00:
    print(f"{nome},Voce esta com sobrepeso cuide-se") 
else:
    print(f"{nome},Seu peso esta normal, continue assim")
print(imc)
