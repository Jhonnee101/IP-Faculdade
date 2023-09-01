clientes = []
def cadastro_cliente():
    nome = input("Nome do cliente:")
    renda = float(input("Renda:"))
    uf = input("UF:")
    clientes.append([nome, renda, uf])

def listar_renda_superior():
    for cliente in clientes:
        if cliente[1] > 2000 and cliente[2] == "PE":
            print("Nome", cliente[0], "Renda", cliente[1], "UF", cliente[2])

def listar_renda_inferior():
    valor = float(input("Informe o valor inferior para listagem:"))
    uf_um = input("Informe a primeira UF para listagem:")
    uf_dois = input("Informe a segunda UF para listagem:")
    for cliente in clientes:
        if cliente[1] < valor:
            if cliente[2] == uf_um or cliente[2] == uf_dois:
                print("Nome", cliente[0], "Renda", cliente[1], "UF", cliente[2])

def main():
    while True:
        print("[1] Cadastro do cliente")
        print("[2] Listagem renda superior")
        print("[3] Listagem renda inferior")
        opcao = str(input("opcao: "))
        if opcao == "1":
            cadastro_cliente()
        elif opcao == "2":
            listar_renda_superior()
        elif opcao == "3":
            listar_renda_inferior()

main()
    