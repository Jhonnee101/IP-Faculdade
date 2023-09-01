def cadastrar_mercadoria(mercadorias):
    nome = input("Digite o nome da mercadoria: ")
    preco = float(input("Digite o preço da mercadoria: "))
    perecivel = input("A mercadoria é perecível? (Sim/Não): ").lower() == "sim"
    mercadorias[nome] = {"preco": preco, "perecivel": perecivel}

def listar_mercadorias_pereciveis(mercadorias):
    print("Mercadorias perecíveis:")
    for nome, dados in mercadorias.items():
        if dados["perecivel"]:
            print(f"Nome: {nome}, Preço: R$ {dados['preco']:.2f}")

def mostrar_maior_menor_preco(mercadorias):
    maior_mercadoria = max(mercadorias, key=lambda x: mercadorias[x]["preco"])
    menor_mercadoria = min(mercadorias, key=lambda x: mercadorias[x]["preco"])

    print(f"Mercadoria com maior preço: {maior_mercadoria} - R$ {mercadorias[maior_mercadoria]['preco']:.2f}")
    print(f"Mercadoria com menor preço: {menor_mercadoria} - R$ {mercadorias[menor_mercadoria]['preco']:.2f}")

def main():
    mercadorias = {}

    while True:
        print("\n1. Cadastrar mercadoria")
        print("2. Listar mercadorias perecíveis")
        print("3. Mostrar mercadoria com maior e menor preço")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_mercadoria(mercadorias)
            print("Mercadoria cadastrada com sucesso!")

        elif opcao == "2":
            listar_mercadorias_pereciveis(mercadorias)

        elif opcao == "3":
            mostrar_maior_menor_preco(mercadorias)

        elif opcao == "4":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Escolha novamente.")

    main()