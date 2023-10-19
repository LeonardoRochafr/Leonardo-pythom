numero1 = int(input("Digite o primeiro lado do triângulo: "))
numero2 = int(input("Digite o segundo lado do triângulo: "))
numero3 = int(input("Digite o terceiro lado do triângulo: "))

# Verifica se é um triângulo
if numero1 + numero2 > numero3 and numero1 + numero3 > numero2 and numero2 + numero3 > numero1:
    print("É um triângulo")
    
    # Verifica o tipo de triângulo
    if numero1 == numero2 == numero3:
        print("É equilátero")
    elif numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
        print("É isósceles")
    else:
        print("É escaleno")
else:
    print("Não é um triângulo")
