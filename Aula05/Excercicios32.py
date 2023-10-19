# Solicita ao usuário o número inteiro para calcular o fatorial
numero = int(input("Digite um número inteiro para calcular o fatorial: "))

# Verifica se o número é não negativo
if numero < 0:
    print("Fatorial é indefinido para números negativos.")
else:
    # Inicializa o resultado do fatorial
    resultado_fatorial = 1

    # Inicializa a string para representar o fatorial
    fatorial_string = f"{numero}! ="

    # Calcula o fatorial do número
    for i in range(numero, 0, -1):
        resultado_fatorial *= i
        fatorial_string += f" {i} ."

    # Remove o último ponto (.) da string
    fatorial_string = fatorial_string[:-1]

    # Exibe o resultado
    print(fatorial_string, "=", resultado_fatorial)
