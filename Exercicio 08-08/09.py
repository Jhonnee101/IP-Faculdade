nomes = []

while True:
    nome = str(input("Digite um nome[Sair para fechar]: "))
    if nome == "Sair":
        break
    else:
        nomes.append(nome)
print(f"O maior nome digitado foi {min(nomes)}")
print(f"O menor nome digitado foi {max(nomes)}")