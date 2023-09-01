def cadastrar_cliente(clientes):
    nome = input("Digite o nome do cliente: ")
    renda = float(input("Digite a renda do cliente: "))
    uf = input("Digite o UF do cliente: ")
    clientes.append({"nome": nome, "renda": renda, "uf": uf})

def mostrar_clientes_renda_superior(clientes):
    print("Clientes com renda superior a R$ 2.000,00 do estado de Pernambuco:")
    for cliente in clientes:
        if cliente["renda"] > 2000 and cliente["uf"] == "PE":
            print(f"Nome: {cliente['nome']}, Renda: R$ {cliente['renda']:.2f}, UF: {cliente['uf']}")

def mostrar_clientes_renda_inferior(clientes, valor_limite):
    print(f"Clientes com renda inferior a R$ {valor_limite:.2f}:")
    for cliente in clientes:
        if cliente["renda"] < valor_limite:
            print(f"Nome: {cliente['nome']}, Renda: R$ {cliente['renda']:.2f}, UF: {cliente['uf']}")

def main():
    lista_clientes = []

    while True:
        print("\n1. Cadastrar cliente")
        print("2. Mostrar clientes com renda superior a R$ 2.000,00 de Pernambuco")
        print("3. Mostrar clientes com renda inferior a um determinado valor")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente(lista_clientes)
            print("Cliente cadastrado com sucesso!")

        elif opcao == "2":
            mostrar_clientes_renda_superior(lista_clientes)

        elif opcao == "3":
            valor_limite = float(input("Digite o valor limite de renda: "))
            mostrar_clientes_renda_inferior(lista_clientes, valor_limite)

        elif opcao == "4":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Escolha novamente.")


main()