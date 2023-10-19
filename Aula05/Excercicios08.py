# Inicializa variáveis para a soma e a média
soma = 0
media = 0

# Loop para ler 5 números
for i in range(5):
    numero = float(input(f"Digite o {i + 1}º número: "))
    soma += numero

# Calcula a média
media = soma / 5

# Exibe a soma e a média
print(f"A soma dos números é: {soma}")
print(f"A média dos números é: {media}")
