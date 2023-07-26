def calcular_nota(porcentagem):
    if porcentagem >= 90:
        return 'A'
    elif porcentagem >= 80:
        return 'B'
    elif porcentagem >= 70:
        return 'C'
    elif porcentagem >= 60:
        return 'D'
    else:
        return 'F'

porcentagem = float(input("Digite seu percentual de pontos: "))
print("Sua nota é:", calcular_nota(porcentagem))