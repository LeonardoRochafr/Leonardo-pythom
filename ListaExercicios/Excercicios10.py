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