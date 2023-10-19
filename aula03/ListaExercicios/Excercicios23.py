#numero inteiro ou decimal, função arrendoda

# Solicita ao usuário que digite um número
numero = input("Digite um número: ")
numero = float(numero)

numero_arredondado = round(numero)

if numero == numero_arredondado:
    print("O número é inteiro.")
else:
    print("O número é decimal.")
