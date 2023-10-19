#Faça um programa que leia 5 números e informe o maior número

maior_numero = float('-inf')

for i in range(5):
    numero = float(input(f"Digite um numero {i+1} "))
    if numero > maior_numero:
        maior_numero = numero

print(f" o maior número é: {maior_numero}")

