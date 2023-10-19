#numero menor
numero1 = input("digite o primeiro")
numero2 = input("digite o segundo")
numero3 = input("digite o terceiro")

numero1 = int(numero1)
numero2 = int(numero2)
numero3 = int(numero3)

if numero1<numero2 and numero1 < numero3:
    print(numero1,"é o menor número")

elif numero2<numero1 and numero2 < numero3:
    print(numero2,"é o menor número")

elif numero3<numero1 and numero3 < numero2:
    print(numero3,"é o menor número")

else:
    print("você digitou dois ou três numeros iguais")