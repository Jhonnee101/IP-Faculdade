def eh_consoante(caractere):
    vogais = ['a', 'e', 'i', 'o', 'u']
    if caractere in vogais:
        return 1
    else:
        return 0

caractere=input('Digite o caractere ')
print(eh_consoante(caractere))