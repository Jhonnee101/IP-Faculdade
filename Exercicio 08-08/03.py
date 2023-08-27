lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9]

def concatenar_listas(lista1,lista2):
    concatenar = lista1 + lista2
    print(f"A concatenacao das duas listas ficou {concatenar}")
    return concatenar

def main():
    chamar = concatenar_listas(lista1,lista2)
main()
