#calculo do salário na folha de pagamento:

descontoIR = 0.0
descontoINSS = 0.0
fgts = 0.0
salarioBruto = 0.0
descSindicato = 0.0
percSindicato = 0.03
percFGTS = 0.11
percIR = 0
salarioLiquido = 0.0
totalDesconto = 0.0

valorHora = float(input("Digite o valor da hora: "))
horasTrabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))

salarioBruto = valorHora * horasTrabalhadas

if salarioBruto > 900 and salarioBruto <= 1500:
    percIR = 5
elif salarioBruto <= 2500:
    percIR = 10
else:
    percIR = 20
    
fgts = salarioBruto * percFGTS
descSindicato = salarioBruto * percSindicato
descontoINSS = salarioBruto * 0.10
descontoIR = salarioBruto * (percIR/100)  
totalDesconto = descontoINSS + descontoIR  
salarioLiquido =  salarioBruto - descontoIR - descontoINSS 

print("Salário Bruto: (", valorHora , " * " , horasTrabalhadas, ")        : R$ " , salarioBruto)
print("(-) IR (",percIR,"%)                     : R$ ",   descontoIR)  
print("(-) INSS ( 10%)                 : R$ ", descontoINSS)
print("FGTS (11%)                      : R$ ", fgts)
print("Total de descontos              : R$ ", totalDesconto)
print("Salário Liquido                 : R$ ", salarioLiquido)