import json

def load_contacts():
    try:
        with open('contatos.json', 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    return contacts

def save_contacts(contacts):
    with open('contatos.json', 'w') as file:
        json.dump(contacts, file, indent=4)

def cadastrar_contato(contacts):
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    novo_contato = {"nome": nome, "telefone": telefone, "email": email}
    contacts.append(novo_contato)
    save_contacts(contacts)
    print("Contato cadastrado com sucesso!")

def exibir_contatos(contacts):
    print("Lista de Contatos:")
    for index, contato in enumerate(contacts, start=1):
        print(f"{index}. Nome: {contato['nome']}, Telefone: {contato['telefone']}, E-mail: {contato['email']}")

def pesquisar_contato(contacts, nome):
    for contato in contacts:
        if contato["nome"].lower() == nome.lower():
            print("Informações do Contato:")
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, E-mail: {contato['email']}")
            return
    print("Contato não encontrado.")

contatos = load_contacts()

while True:
    print("\nMenu:")
    print("[1] Cadastrar contato")
    print("[2] Exibir contatos")
    print("[3] Pesquisar contato")
    print("[4] Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        cadastrar_contato(contatos)
    elif opcao == "2":
        exibir_contatos(contatos)
    elif opcao == "3":
        nome_pesquisa = input("Digite o nome do contato: ")
        pesquisar_contato(contatos, nome_pesquisa)
    elif opcao == "4":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Escolha uma opção válida.")
