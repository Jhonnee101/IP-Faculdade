produto = str(input("Digite o nome do produto: "))
quantidade = int(input("Digite a quantidade de produtos: "))
valor = float(input("Digite o valor do produto: "))
preco = valor * quantidade
print(f"O produto selecionado foi {produto}, e o seu valor final ficou de {preco} pois voce pegou {quantidade} unidades")
