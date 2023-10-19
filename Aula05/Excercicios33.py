# Inicializa as variáveis para a menor e maior temperatura
menor_temperatura = None
maior_temperatura = None

# Inicializa a variável para a soma das temperaturas
soma_temperaturas = 0

# Inicializa a variável para contar o número de temperaturas
contador_temperaturas = 0

# Solicita ao usuário inserir a primeira temperatura
temperatura = float(input("Digite a temperatura (ou um valor negativo para encerrar): "))

while temperatura >= 0:
    # Atualiza a soma das temperaturas
    soma_temperaturas += temperatura

    # Atualiza a menor temperatura
    if menor_temperatura is None or temperatura < menor_temperatura:
        menor_temperatura = temperatura
    
    # Atualiza a maior temperatura
    if maior_temperatura is None or temperatura > maior_temperatura:
        maior_temperatura = temperatura

    contador_temperaturas += 1

    # Solicita ao usuário inserir a próxima temperatura
    temperatura = float(input("Digite a próxima temperatura (ou um valor negativo para encerrar): "))

if contador_temperaturas > 0:
    # Calcula a média das temperaturas
    media_temperaturas = soma_temperaturas / contador_temperaturas

    # Exibe os resultados
    print(f"Menor temperatura: {menor_temperatura}")
    print(f"Maior temperatura: {maior_temperatura}")
    print(f"Média das temperaturas: {media_temperaturas:.2f}")
else:
    print("Nenhuma temperatura válida foi informada.")
