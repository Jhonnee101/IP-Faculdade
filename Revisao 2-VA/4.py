
def cadastrar_animal(animais, nome, raca, peso):
    novo_animal = {"nome": nome, "raca": raca, "peso": peso}
    animais.append(novo_animal)
    print(f"Animal '{nome}' cadastrado com sucesso!")

def listar_animais_por_raca(animais, raca):
    animais_raca = [animal for animal in animais if animal["raca"] == raca]
    if len(animais_raca) == 0:
        print(f"Nenhum animal da raça '{raca}' encontrado.")
    else:
        print(f"Animais da raça '{raca}':")
        for animal in animais_raca:
            print(f"Nome: {animal['nome']}, Peso: {animal['peso']} kg")


def calcular_media_peso_por_raca(animais, raca):
    animais_raca = [animal for animal in animais if animal["raca"] == raca]
    if len(animais_raca) == 0:
        print(f"Nenhum animal da raça '{raca}' encontrado para calcular a média de peso.")
        return 0
    else:
        pesos = [animal["peso"] for animal in animais_raca]
        media_peso = sum(pesos) / len(animais_raca)
        return media_peso

animais = []

while True:
    print("\nOpções:")
    print("1. Cadastrar animal")
    print("2. Listar animais de uma raça")
    print("3. Calcular média de peso por raça")
    print("4. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome = input("Digite o nome do animal: ")
        raca = input("Digite a raça do animal: ")
        peso = float(input("Digite o peso do animal em kg: "))
        cadastrar_animal(animais, nome, raca, peso)
    elif escolha == "2":
        raca = input("Digite a raça para listar os animais: ")
        listar_animais_por_raca(animais, raca)
    elif escolha == "3":
        raca = input("Digite a raça para calcular a média de peso: ")
        media_peso = calcular_media_peso_por_raca(animais, raca)
        if media_peso != 0:
            print(f"A média de peso dos animais da raça '{raca}' é {media_peso:.2f} kg.")
    elif escolha == "4":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
