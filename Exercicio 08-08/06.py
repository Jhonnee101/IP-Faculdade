def eh_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def verifica_primos_lista(lista):
    primos = []
    for numero in lista:
        if eh_primo(numero):
            primos.append(numero)
    return primos

numeros = [2, 3, 5, 7, 10, 11, 13, 16, 17, 19]
primos_encontrados = verifica_primos_lista(numeros)
print(primos_encontrados)