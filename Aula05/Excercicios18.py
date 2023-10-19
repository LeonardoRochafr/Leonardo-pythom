# Solicita ao usuário a quantidade de números
N = int(input("Digite a quantidade de números a serem inseridos: "))

# Inicializa variáveis para o menor, maior e soma
menor_valor = None
maior_valor = None
soma_valores = 0

# Loop para pedir N números
for i in range(N):
    numero = float(input(f"Digite o {i + 1}º número: "))

    # Atualiza o menor e o maior valor
    if menor_valor is None or numero < menor_valor:
        menor_valor = numero
    if maior_valor is None or numero > maior_valor:
        maior_valor = numero

    # Soma os valores
    soma_valores += numero

# Exibe o resultado
print(f"Menor valor: {menor_valor}")
print(f"Maior valor: {maior_valor}")
print(f"Soma dos valores: {soma_valores}")
