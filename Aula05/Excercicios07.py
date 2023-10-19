# Inicializa a variável para armazenar o maior número
maior_numero = None

# Loop para ler 5 números
for i in range(5):
    numero = float(input(f"Digite o {i + 1}º número: "))
    if maior_numero is None or numero > maior_numero:
        maior_numero = numero

# Exibe o maior número
print(f"O maior número entre os 5 números é: {maior_numero}")
