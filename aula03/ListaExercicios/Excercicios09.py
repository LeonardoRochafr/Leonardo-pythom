#ler 3 números e falar em ordem decrecente

numero1 = int(input("digite o primeiro"))
numero2 = int(input("digite o segundo"))
numero3 = int(input("digite o terceiro"))

if numero1 >= numero2 and numero1 >= numero3:
    maior = numero1
    if numero2 >= numero3:
        meio = numero2
        menor = numero3
    else:
        meio = numero3
        menor = numero2

elif numero2 >= numero1 and numero2 >= numero3:
    maior = numero2
    if numero1 >= numero3:
        meio = numero1
        menor = numero3
    else:
        meio = numero3
        menor = numero1

else:
    maior = numero3
    if numero1 >= numero2:
        meio = numero1
        menor = numero2
    else:
        meio = numero2
        menor = numero1

print(maior,",",meio,",",menor)

