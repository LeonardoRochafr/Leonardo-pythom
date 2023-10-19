#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades

numero = int(input("Digite um número inteiro menor que 1000: "))

if numero < 0 or numero >= 1000:
    print("Número fora do intervalo permitido.")
else:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    #(singular ou plural)
    if centenas == 1:
        centenas_str = "centena"
    else:
        centenas_str = "centenas"
    
    if dezenas == 1:
        dezenas_str = "dezena"
    else:
        dezenas_str = "dezenas"
    
    if unidades == 1:
        unidades_str = "unidade"
    else:
        unidades_str = "unidades"

    print(f"{numero} = {centenas} {centenas_str}, {dezenas} {dezenas_str} e {unidades} {unidades_str}")
