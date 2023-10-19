# Solicita ao usuário a quantidade de turmas
quantidade_turmas = int(input("Digite a quantidade de turmas: "))

# Inicializa a variável para o total de alunos
total_alunos = 0

# Loop para pedir a quantidade de alunos em cada turma
for turma in range(1, quantidade_turmas + 1):
    while True:
        quantidade_alunos = int(input(f"Digite a quantidade de alunos na turma {turma}: "))
        if 1 <= quantidade_alunos <= 40:
            total_alunos += quantidade_alunos
            break
        else:
            print("A quantidade de alunos em uma turma deve estar entre 1 e 40. Tente novamente.")

# Calcula o número médio de alunos por turma
media_alunos_por_turma = total_alunos / quantidade_turmas

# Exibe o resultado
print(f"O número médio de alunos por turma é: {media_alunos_por_turma}")
