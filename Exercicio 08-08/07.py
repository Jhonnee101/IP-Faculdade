lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 5, 7, 10, 11, 13, 16, 17, 19,
         1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 5, 7, 10, 11, 13, 16, 17, 19,]

for count in range(0,19):
    countador = count + 1
    if count >0:
        print(f"O numero {count} apareceu {lista.count(countador)} vezes")
    else:
        print("")