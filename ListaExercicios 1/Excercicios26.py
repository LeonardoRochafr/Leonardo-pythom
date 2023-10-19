# Solicita o número de litros vendidos e o tipo de combustível ao usuário
litros = float(input("Digite o número de litros vendidos: "))
combustivel = input("Digite o tipo de combustível (A - Álcool / G - Gasolina): ")

# Preços por litro
preco_alcool = 1.90
preco_gasolina = 2.50

if combustivel == 'A' or combustivel == 'a':
    if litros <= 20:
        valor = litros * preco_alcool * 0.97  # 3% de desconto
    else:
        valor = litros * preco_alcool * 0.95  # 5% de desconto
elif combustivel == 'G' or combustivel == 'g':
    if litros <= 20:
        valor = litros * preco_gasolina * 0.96  # 4% de desconto
    else:
        valor = litros * preco_gasolina * 0.94  # 6% de desconto
else:
    print("Tipo de combustível inválido.")
    valor = 0  # Valor zerado para tipos de combustível inválidos

if valor > 0:
    print(f"Total a ser pago: R$ ",valor)
