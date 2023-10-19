# Solicita ao usuário os dois números inteiros
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

# Verifica qual é o menor e o maior número
menor_numero = min(numero1, numero2)
maior_numero = max(numero1, numero2)

# Inicializa a variável para a soma
soma = 0

# Loop for para gerar os números no intervalo e calcular a soma
print(f"Números no intervalo entre {menor_numero} e {maior_numero}:")
for numero in range(menor_numero, maior_numero + 1):
    print(numero)
    soma += numero

# Exibe a
