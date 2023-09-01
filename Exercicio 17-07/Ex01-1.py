def menu():
    print('''[1] - Verificar folha de pagamento
    [2] - Sair''')
    opcao = int(input("Opçao: "))
    return opcao

def mostrarSalario(salario, dependentes):
    salariototal = salario
    salariofinal = dependentes * 50
    print("Salario Total: ", salariototal)
    print("Salario com o auxilio: ", salariofinal)

def calcularFolha(nome, salario, dependentes):
    mostrarSalario(salario, dependentes)

def finalizarAplicacao():
    print("Aplicaçao finalizada")


def main():
    while True:
        opcaoMenu = menu()
        if opcaoMenu == 1:
            nome = str(input("Nome do funcionário: "))
            salario = float(input("Salario Bruto: "))
            dependentes = int(input("Numero de Dependentes: "))
            calcularFolha(nome, salario, dependentes)
        else:
            finalizarAplicacao()
            break

main()