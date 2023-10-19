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
