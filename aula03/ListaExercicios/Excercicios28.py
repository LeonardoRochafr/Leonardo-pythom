
tipo_carne = input("Digite o tipo de carne (File Duplo, Alcatra ou Picanha): ")
quantidade = float(input("Digite a quantidade de carne (em Kg): "))
forma_pagamento = input("Digite a forma de pagamento (cartão Tabajara ou outro): ")


preco_file_duplo = 4.90 if quantidade <= 5 else 5.80
preco_alcatra = 5.90 if quantidade <= 5 else 6.80
preco_picanha = 6.90 if quantidade <= 5 else 7.80


valor_total = 0.0

if tipo_carne.lower() == "file duplo":
    valor_total = quantidade * preco_file_duplo
elif tipo_carne.lower() == "alcatra":
    valor_total = quantidade * preco_alcatra
elif tipo_carne.lower() == "picanha":
    valor_total = quantidade * preco_picanha
else:
    print("Tipo de carne inválido.")

# Aplicar desconto de 5% se for cartão Tabajara
desconto = 0.0

if forma_pagamento.lower() == "cartão tabajara":
    desconto = valor_total * 0.05


valor_a_pagar = valor_total - desconto

# Exibir cupom fiscal
print("Cupom Fiscal:")
print("Tipo de carne:", tipo_carne)
print("Quantidade:",quantidade,"Kg")
print("Preço total: R$",valor_total)
print("Forma de pagamento:", forma_pagamento)
print("Desconto: R$", desconto)
print("Valor a pagar: R$", valor_a_pagar)

