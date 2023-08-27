def separa_positivos_negativos(lista):
    positivos = []
    negativos = []
    
    for numero in lista:
        if numero > 0:
            positivos.append(numero)
        elif numero < 0:
            negativos.append(numero)
    
    return positivos, negativos

numeros = [-2, 5, -10, 8, -3, 0, 7]
positivos, negativos = separa_positivos_negativos(numeros)

print("Números positivos:", positivos)
print("Números negativos:", negativos)