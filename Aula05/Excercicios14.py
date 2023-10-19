# Variáveis para contar os números pares e ímpares
quantidade_pares = 0
quantidade_impares = 0

# Loop for para pedir 10 números inteiros
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))

    # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        quantidade_pares += 1
    else:
        quantidade_impares += 1

# Exibe a quantidade de números pares e ímpares
print("Quantidade de números pares:", quantidade_pares)
print("Quantidade de números ímpares:", quantidade_impares)
