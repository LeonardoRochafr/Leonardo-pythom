#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime:

print("Responda 'sim' ou 'não' para as seguintes perguntas:")
pergunta1 = input("Telefonou para a vítima? ")
pergunta2 = input("Esteve no local do crime? ")
pergunta3 = input("Mora perto da vítima? ")
pergunta4 = input("Devia para a vítima? ")
pergunta5 = input("Já trabalhou com a vítima? ")

contagem_respostas_positivas = 0

if pergunta1.lower() == "sim":
    contagem_respostas_positivas += 1

if pergunta2.lower() == "sim":
    contagem_respostas_positivas += 1

if pergunta3.lower() == "sim":
    contagem_respostas_positivas += 1

if pergunta4.lower() == "sim":
    contagem_respostas_positivas += 1

if pergunta5.lower() == "sim":
    contagem_respostas_positivas += 1

# CLASSIFICAÇÃO
if contagem_respostas_positivas == 2:
    print("Suspeita")
elif contagem_respostas_positivas == 3 or contagem_respostas_positivas == 4:
    print("Cúmplice")
elif contagem_respostas_positivas == 5:
    print("Assassino")
else:
    print("inocente")
