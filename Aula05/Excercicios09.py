#  for para imprimir os números ímpares entre 1 e 50
print("Números ímpares entre 1 e 50:")
for numero in range(1, 51):
    if numero % 2 != 0:  # Verifica se o número é ímpar (resto da divisão por 2 não é igual a zero)
        print(numero)
