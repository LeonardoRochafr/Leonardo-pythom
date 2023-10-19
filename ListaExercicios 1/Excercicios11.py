# programa que reajuste o salário dos colaboradores 
salario = input("digite o salário")
salario = int(salario)


if salario <= 280:
    print("antes do reajuste:", salario)
    print ("depois do reajuste o salario foi de:",salario + salario/5)
    print("o percentual do aumento foi de 20%")
    reajuste = salario * 0,20
    print ("o reajuste foi de:", reajuste)
   
elif salario > 280 and salario < 700: 
    print ("antes do reajuste:", salario)
    print ("depois do reajuste o salario foi de:",salario + (salario * 0.15))
    print("o percentual do aumento foi de 15%")
    reajuste = salario * 0,15
    print("o reajuste foi de",reajuste)

elif salario > 700 and salario < 1500: 
    print("antes do reajuste:",salario)
    print ("depois do reajuste o salario foi de:",salario + (salario * 0.10))
    print("o percentual do aumento foi de 10%")
    reajuste = salario * 0,10
    print("o reajuste foi de",reajuste)

elif salario > 1500:
    print("antes do reajuste",salario) 
    print ("depois do reajuste o salario foi de:",salario + (salario * 0.05))
    print("o percentual do aumento foi de 5%")
    reajuste = salario * 0.05
    print("o reajuste foi de", reajuste)
    