
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Escolha uma operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
operacao = int(input("Digite o número da operação desejada: "))

if operacao == 1:
    resultado = num1 + num2

elif operacao == 2:
    resultado = num1 - num2

elif operacao == 3:
    resultado = num1 * num2

elif operacao == 4:
    if num2 == 0:
        print("Erro: Divisão por zero.")
        
    else:
        resultado = num1 / num2
else:
    print("Operação inválida.")

# par ou ímpar
if resultado % 2 == 0:
    tipo_par_impar = "par"
else:
    tipo_par_impar = "ímpar"

# positivo ou negativo
if resultado > 0:
    tipo_positivo_negativo = "positivo"
elif resultado < 0:
    tipo_positivo_negativo = "negativo"
else:
    tipo_positivo_negativo = "zero"
