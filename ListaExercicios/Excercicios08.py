#preço do produto / qual devo comprar (o mais barato)
numero1 = input("digite o preço do primeiro produto")
numero2 = input("digite o preço do segundo produto")
numero3 = input("digite o preço do terceiro produto")

if numero1<numero2 and numero1<numero3 :
    print(" o primeiro produto é o mas barato")

elif numero2<numero1 and numero2<numero3:
    print(" o segundo produto é o mais barato")

elif numero3<numero2 and numero3<numero1:
    print("o terceiro produto é o mais barato")
