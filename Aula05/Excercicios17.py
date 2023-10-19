# Solicita ao usuário o número inteiro para calcular o fatorial
numero = int(input("Digite um número inteiro para calcular o fatorial: "))

# Inicializa a variável para armazenar o resultado do fatorial
fatorial = 1

# Calcula o fatorial do número
if numero < 0:
    print("Não é possível calcular o fatorial de um número negativo.")
elif numero == 0:
    print("O fatorial de 0 é 1.")
else:
    for i in range(1, numero + 1):
        fatorial *= i

    # Exibe o resultado
    print(f"{numero}! = {fatorial}")
