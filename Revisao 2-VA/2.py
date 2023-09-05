def informacoes_listas(lista_inteiros, lista_reais, lista_caracteres):
    soma_inteiros = sum([num for num in lista_inteiros if 10 <= num <= 40])

    vogais_a = lista_caracteres.count('A') + lista_caracteres.count('a')

    if len(lista_reais) > 0:
        media_reais = sum(lista_reais) / len(lista_reais)
    else:
        media_reais = 0

    print(f"1. Soma dos valores inteiros entre 10 e 40: {soma_inteiros}")
    print(f"2. Quantidade de vogais 'A' na lista de caracteres: {vogais_a}")
    print(f"3. Média dos valores reais: {media_reais:.2f}")


lista_inteiros = [5, 15, 25, 35, 45]
lista_reais = [12.5, 20.3, 15.7, 30.2]
lista_caracteres = ['A', 'B', 'a', 'C', 'D', 'E']

informacoes_listas(lista_inteiros, lista_reais, lista_caracteres)