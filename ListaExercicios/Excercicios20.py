
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
