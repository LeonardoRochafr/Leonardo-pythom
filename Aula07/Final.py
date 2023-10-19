# Criar um menu para mostrar as funções disponíveis e o usuário selecionar qual
# função ele quer executar.

# Faça um Programa que peça dois números e imprima o maior deles.

def imprimir_maior_numero():
    numero1 = input("Digite o primeiro número: ")

    numero2 = input("Digite o segundo número: ")

    try:
        numero1 = int(numero1)
        numero2 = int(numero2)
        if numero1 > numero2:
            print("O número", numero1, "é maior que o número", numero2)
        elif numero1 == numero2:
            print("Os números são iguais")
        else:
            print("O número", numero2, "é maior que o número", numero1)
    except Exception:
        print("Você não digitou um número válido")
        exit()


def verificar_valor_positivo():
    # Faça um Programa que peça um valor e mostre na tela se o valor é positivo 
    # ou negativo.

    valor = int(input("Digite um valor: "))

    if valor > 0:
        print("O valor é positivo")
    elif valor == 0:
        print("O valor é neutro")
    else:
        print("O valor é negativo")

# Criar um menu para mostrar as funções disponíveis e o usuário selecionar qual
# função ele quer executar.

def maior_que():

            numero1 = input("digite um número")
            numero2 = input("digite outro número")

            numero1 = int(numero1)
            numero2 = int(numero2)
            if numero1 > numero2:
                print(numero1,"é maior que", numero2)
            elif numero1 < numero2:
                print(numero2,"é maior que",numero1)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def mas_fem():
#masculino ou feminino

    numero4 = input ("digite M ou F")  

    if numero4 == "M" or "m" == numero4:
     print ("Masculino")

    elif numero4 == "F" or "f" == numero4:
        print("Feminino")
    else:
        print("sexo invalido")
        

def vogal_consoante():
      # a letra é vogal ou consoante
    letra = input("Digite um letra")

    if letra.lower () in ('a','e','i','o','u'):
        print("A letra", letra, "é uma vogal")
    elif letra in ('1','2','3','4','5', '6' , '7', '8' , '9', '0'):
        print("você digitou um número")
    else:
        print("A Letra", letra, "é uma consoante")

def duas_medias():
    #duas medias de um aluno

    nota1 = input("Digite a primeira nota: ")
    nota2 = input("Digite a segunda nota: ")

    # Converter as notas para números inteiros
    nota1 = int(nota1)
    nota2 = int(nota2)

    # Calcular a média das notas
    media = (nota1 + nota2) / 2

    if media == 10:
        print("Aprovado com distinção")
    elif media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

    #três números, qual o maior

def tres_maior():
    numero1 = input("digite o primeiro")
    numero2 = input("digite o segundo")
    numero3 = input("digite o terceiro")

    numero1 = int(numero1)
    numero2 = int(numero2)
    numero3 = int(numero3)

    if numero1>numero2 and numero1 > numero3:
        print(numero1,"é o maior número")

    elif numero2>numero1 and numero2 > numero3:
        print(numero2,"é o maior número")

    elif numero3>numero1 and numero3 > numero2 :
        print(numero3,"é o maior número")

    else:
        print("você digitou dois numero iguais")

def numero_menor():
    #numero menor
    numero1 = input("digite o primeiro")
    numero2 = input("digite o segundo")
    numero3 = input("digite o terceiro")

    numero1 = int(numero1)
    numero2 = int(numero2)
    numero3 = int(numero3)

    if numero1<numero2 and numero1 < numero3:
        print(numero1,"é o menor número")

    elif numero2<numero1 and numero2 < numero3:
        print(numero2,"é o menor número")

    elif numero3<numero1 and numero3 < numero2:
        print(numero3,"é o menor número")

    else:
        print("você digitou dois ou três numeros iguais")

def produto_barato():
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

def ordem_decrecente():
    #ler 3 números e falar em ordem decrecente

    numero1 = int(input("digite o primeiro"))
    numero2 = int(input("digite o segundo"))
    numero3 = int(input("digite o terceiro"))

    if numero1 >= numero2 and numero1 >= numero3:
        maior = numero1
        if numero2 >= numero3:
            meio = numero2
            menor = numero3
        else:
            meio = numero3
            menor = numero2

    elif numero2 >= numero1 and numero2 >= numero3:
        maior = numero2
        if numero1 >= numero3:
            meio = numero1
            menor = numero3
        else:
            meio = numero3
            menor = numero1

    else:
        maior = numero3
        if numero1 >= numero2:
            meio = numero1
            menor = numero2
        else:
            meio = numero2
            menor = numero1

    print(maior,",",meio,",",menor)

def turno_estuda():
        #turno em que estuda, matutino /
    turno = input("escreva o turno em que você estuda (M,V ou N): ")

    if turno.upper() == 'M':
        print("bom dia")
    elif turno.upper() == 'V':
        print("boa tarde")
    elif turno.upper () == 'N':
        print("boa noite")
    else:
        print("você digitou invalido")


def reajuste_salario():
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
    
def folha_pagamento():
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

def dia_semana():
        #faça um programa que leia um número e exiba o dia correspondente da semana

    dia = input ("digite um número")
    # dia = int(dia)

    if dia in ('1','8','15','22','29'):
        print("é segunda feira")

    elif dia in ('2','9','16','23','30'):
        print("é terça feira")

    elif dia in ('3','10','17','24','31'):
        print("é quarta feira")

    elif dia in ('4','11','18','25'):
        print("é quinta feira")

    elif dia in ('5','12','19','26'):
        print("é sexta feira")

    elif dia in ('6','13','20','27'):
        print("é sabado")

    elif dia in ('7','14','21','28'):
        print("é  domingo")

    else:
        print("valor invalido")

def notas_parciais():
        #notas parciais do aluno, (A,B,C,D,E) Reprovado ou aprovado

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    mediafinal = (nota1 + nota2) / 2

    if mediafinal >= 9.0 and mediafinal <= 10:
        print("Nota A")
        print("Aprovado")
    elif mediafinal >= 7.5:
        print("Nota B")
        print("Aprovado")
    elif mediafinal >= 6.0:
        print("Nota C")
        print("Aprovado")
    elif mediafinal >= 4.0:
        print("Nota D")
        print("Reprovado")
    else:
        print("Nota E")
        print("Reprovado")

def lados_triangulo():
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

def bhaskara():
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

def bissexto():
        # digite um ano, é bissexto ou não

    ano = int(input("Digite um ano: "))

    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(ano ,"é um ano bissexto.")
    else:
        print(ano, "não é um ano bissexto.")

def centenas_dezenas_unidades():  
        #Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades

    numero = int(input("Digite um número inteiro menor que 1000: "))

    if numero < 0 or numero >= 1000:
        print("Número fora do intervalo permitido.")
    else:
        centenas = numero // 100
        dezenas = (numero % 100) // 10
        unidades = numero % 10

        #(singular ou plural)
        if centenas == 1:
            centenas_str = "centena"
        else:
            centenas_str = "centenas"
        
        if dezenas == 1:
            dezenas_str = "dezena"
        else:
            dezenas_str = "dezenas"
        
        if unidades == 1:
            unidades_str = "unidade"
        else:
            unidades_str = "unidades"

        print(f"{numero} = {centenas} {centenas_str}, {dezenas} {dezenas_str} e {unidades} {unidades_str}")

def parcial_tres_notas():
    
    nota1 = input("Digite a primeira nota: ")
    nota2 = input("Digite a segunda nota: ")
    nota3 = input("digite a terceira nota")

    nota1 = int(nota1)
    nota2 = int(nota2)
    nota3 = int(nota3)

    media = (nota1 + nota2 + nota3) / 3

    if media == 10:
        print("Aprovado com distinção")
    elif media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

def caixa_eletronico():
        #Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois 
    #informar quantas notas de cada valor serão

    saque = int(input("Digite o valor do saque (entre 10 e 600 reais): "))

    if saque < 10 or saque > 600:
        print("Valor de saque fora do intervalo permitido.")
    else:
        # quant. notas
        notas_de_100 = saque // 100
        saque %= 100

        notas_de_50 = saque // 50
        saque %= 50

        notas_de_10 = saque // 10
        saque %= 10

        notas_de_5 = saque // 5
        saque %= 5

        notas_de_1 = saque

        print("Notas de 100 reais:",notas_de_100)
        print("Notas de 50 reais:", notas_de_50)
        print("Notas de 10 reais:", notas_de_10)
        print("Notas de 5 reais:", notas_de_5)
        print("Notas de 1 real:", notas_de_1)


def par_impar():
    # numero inteiro é par ou impar

    numero = int(input("digite um número inteiro"))
    numero02 = 2

    if int(numero) % numero02  == 0:
        print("é par")

    else:
        int(numero) % numero02 !=0
        print("é impar")

def inteiro_decimal():
        #numero inteiro ou decimal, função arrendoda

    # Solicita ao usuário que digite um número
    numero = input("Digite um número: ")
    numero = float(numero)

    numero_arredondado = round(numero)

    if numero == numero_arredondado:
        print("O número é inteiro.")
    else:
        print("O número é decimal.")

def soma_divisao():
    
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




def menu():


    opcao = 1  
    while opcao != 0:
        print('----Seja bem vindo ao meu Super Menu----')
        print('Escolha uma opção abaixo:')
        print('1 - Imprimir maior número')
        print('2 - Verificar se o valor é positivo ou negativo')
        
        print('\n3 - Iniciando função masculino ou feminino')
        print('5 - Função duas medias de um aluno')
        print('6 - Função três numeros qual o maior')
        print('7 - Função três numeros qual o menor')
        print('8 - Função produto mais barato')
        print('9 - Função ordem decrecente')
        print('10 - Função turno em que estuda')
        print('11 - Função reajuste do salário')
        print('12 - função calculo da folha de pagamento')
        print('13 - Função dia da semana')
        print('14 - Função notas parciais de um bimestre')
        print('15 - função três lados de um triângulo')
        print('16 - função Bhaskara')
        print('17 - função bissexto')
        print('18 - programa incompleto')
        print('19 - função centenas, dezenas e unidades')
        print('20 - função parcial de três notas')
        print('21 - função caixa eletronico')
        print('22 - função par ou impar')
        print('23 - função inteiro_decimal')
        print('24 - função soma e divisão')



        opcao = int(input('Digite uma das opções ou 0 para sair:'))
        if opcao == 1:
            print('---Iniciando a função imprimir_maior_numero---')
            imprimir_maior_numero()
            print('---Fim da função imprimir_maior_numero---')
        elif opcao == 2:
            print('---Iniciando a função verificar_valor_positivo---')
            verificar_valor_positivo()
            print('---Fim da função verificar_valor_positivo---')

        
        elif opcao == 3:
            print('---iniciando a função mas_fem')
            mas_fem()
        elif opcao == 4:
            print('---iniciando a função vogal_consoante')
            vogal_consoante()
        elif opcao == 5:
            print('---iniciando a função duas_medias')
            duas_medias()
        elif opcao == 6:
            print("--- iniciando a função tres_maior")
            tres_maior()
        elif opcao == 7:
            print('---iniciando qual o menor número')
            numero_menor()
        elif opcao == 8:
            print('--- iniciando qual o mais barato')
            numero_menor()   
        elif opcao == 9:
            print('--- iniciando ler tres numeros em ordem decrecente')
            ordem_decrecente()
        elif opcao == 10:
            print('---  iniciando função turno em que estuda')
            turno_estuda()
        elif opcao == 11:
             print('---  iniciando função reajuste do salario')
             reajuste_salario()

        elif opcao == 12:
            print('---  iniciando função folha de pagamento')
            folha_pagamento()
        elif opcao == 13:
            print('---  iniciando função dias da semana')
            dia_semana()
        elif opcao == 14:
            print('---  iniciando função notas parciais')
            notas_parciais()
        elif opcao == 15:
            print('---  iniciando função lados do triangulo')
            lados_triangulo()
        elif opcao == 16:
            print('---  iniciando função bhaskara')
            bhaskara()
        elif opcao == 17:
            print('---  iniciando função bissexto')
            bissexto()
        
        elif opcao == 19:
            print('---  iniciando função unidades,dezenas e centenas')
            centenas_dezenas_unidades()

        elif opcao == 20:
            print('---  iniciando parcial de três notas')
            parcial_tres_notas()
        elif opcao == 21:
            print('--- iniciando função caixa_eletronico')
            caixa_eletronico()
        elif opcao == 22:
            print('--- iniciando função par ou impar')
            par_impar()
        elif opcao == 23:
            print('--- iniciando função inteiro e decimal')
            inteiro_decimal()
        elif opcao == 24:
            print('--- iniciando função soma e divisão')
            soma_divisao()

        


        else:
            print('Opção inválida')

            print('----Fim do menu ----')

      
menu()