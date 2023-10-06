#calculo de Bhaskara

A = int(input("Digite o valor de a: "))
if A == 0:
    print("A não pode ser zero")
else:
    B = int(input("Digite o valor de b: "))
    C = int(input("Digite o valor de c: "))

    delta = (B**2) - (4*A*C)
    print("Delta =", delta)

    if delta < 0:
        print("O delta não pode ser negativo")
    else:
        raiz = delta ** (1/2)
        if delta == 0:
            print("A função é igual a zero e possui apenas uma raiz")
            x1 = (-B + raiz) / (2*A)
            print("x1 é igual a", x1)
        else:
            print("A raiz tem dois resultados")
            x1 = (-B + raiz) / (2*A)
            x2 = (-B - raiz) / (2*A)
            print("x1 é igual a", x1)
            print("x2 é igual a", x2)



