# Solicita ao usuário a quantidade de notas
N = int(input("Digite a quantidade de notas a serem inseridas: "))

# Inicializa a variável para a soma das notas
soma_notas = 0

# Loop para pedir N notas
for i in range(N):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    soma_notas += nota

# Calcula a média aritmética
media = soma_notas / N

# Exibe o resultado
print(f"A média aritmética das {N} notas é: {media}")
