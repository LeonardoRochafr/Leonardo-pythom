  # a letra é vogal ou consoante
letra = input("Digite um letra")

if letra.lower () in ('a','e','i','o','u'):
    print("A letra", letra, "é uma vogal")
elif letra in ('1','2','3','4','5', '6' , '7', '8' , '9', '0'):
    print("você digitou um número")
else:
    print("A Letra", letra, "é uma consoante")