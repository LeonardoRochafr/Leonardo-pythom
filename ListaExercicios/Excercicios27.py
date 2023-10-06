
peso_morango = float(input("Digite a quantidade de morangos (em Kg): "))
peso_maca = float(input("Digite a quantidade de maçãs (em Kg): "))

preco_morango = 2.50
preco_maca = 1.80

total_morango = peso_morango * preco_morango
total_maca = peso_maca * preco_maca
valor_total = total_morango + total_maca

# desconto
if (peso_morango + peso_maca) > 8 or valor_total > 25:
    desconto = valor_total * 0.10
    valor_total -= desconto

print("Total a ser pago: R$",valor_total)