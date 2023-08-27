lista_numeros = [2,3,5,6,8,7,5,3,1]

def calcula_media(lista_numeros):
    total = sum(lista_numeros)
    media = total / len(lista_numeros)
    print(f"{media:.2f}")
    return media

def main():
    chamar = calcula_media(lista_numeros)
main()