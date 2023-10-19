#Extrutura condicional
# if, elif, else

# if-se
# senão-elif
# senão se - else

if 1 == 1:
    print("1 é igual a 1")
    
else: 
    print("1 não é igual a 1")

#Crie um programa que receba a idade de uma pessoa e verifique se ela é maior de idade ou não

idade = input("Digite sua idade")
if int(idade) < 18:
    print("não é maior de idade")
else: 
    int (idade) >= 18
    print("é maior de idade")

    #crie um programa que receba a idade de pesssoa e verifique se ela
    #é obrigada a votr a votar ou não

#Desafio 1
idade = input("Digite sua idade")

if int(idade) >= 18:
    print("é obrigado a votar")

elif int(idade) >= 16:
    print("não é obrigatorio, mas você pode votar")

else: 
    int (idade) < 16
    print(" não pode votar")

#Desafio 2:
#crie um programa que receba um numero de a 20 e verifique se ele é impar ou par

numero = input("digite um número de 1 a 20")
numero02 = 2


if int(numero) % numero02  ==0:
    print("é par")

else:
    int(numero) % numero02 !=0
    print("é impar")
