nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
media = (nota1 + nota2) /2
if media < 7:
    print("Reprovado")
elif media > 7.0:
    print("Aprovado")
else:
    print("Aprovado com destinção")