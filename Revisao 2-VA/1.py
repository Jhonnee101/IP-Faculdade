def separar_alunos(lista_alunos):
    aprovados = []
    reprovados = []
    acima_de_22_anos = 0

    for aluno in lista_alunos:
        nome, idade, nota = aluno
        if idade > 22:
            acima_de_22_anos += 1
        if nota >= 7.0:
            aprovados.append(aluno)
        else:
            reprovados.append(aluno)

    print(f"Alunos com idade superior a 22 anos: {acima_de_22_anos} alunos")
    return aprovados, reprovados

# Exemplo de utilização:
lista_de_alunos = [("Alice", 24, 8.5), ("Bob", 20, 6.0), ("Carol", 23, 7.8), ("David", 21, 5.5)]
aprovados, reprovados = separar_alunos(lista_de_alunos)

print("Alunos aprovados:")
for aluno in aprovados:
    print(f"{aluno[0]} - Idade: {aluno[1]}, Nota: {aluno[2]}")

print("\nAlunos reprovados:")
for aluno in reprovados:
    print(f"{aluno[0]} - Idade: {aluno[1]}, Nota: {aluno[2]}")