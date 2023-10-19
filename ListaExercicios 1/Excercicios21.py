#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois 
#informar quantas notas de cada valor serão

saque = int(input("Digite o valor do saque (entre 10 e 600 reais): "))

if saque < 10 or saque > 600:
    print("Valor de saque fora do intervalo permitido.")
else:
    # quant. notas
    notas_de_100 = saque // 100
    saque %= 100

    notas_de_50 = saque // 50
    saque %= 50

    notas_de_10 = saque // 10
    saque %= 10

    notas_de_5 = saque // 5
    saque %= 5

    notas_de_1 = saque

    print("Notas de 100 reais:",notas_de_100)
    print("Notas de 50 reais:", notas_de_50)
    print("Notas de 10 reais:", notas_de_10)
    print("Notas de 5 reais:", notas_de_5)
    print("Notas de 1 real:", notas_de_1)
