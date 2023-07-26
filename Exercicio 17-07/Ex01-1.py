from Funcoes import *
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