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
