#faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nome = (input("Digite um nome maior que 3 caracteres: "))


if len(nome) < 3:
    print('menor que 3')
    if len(nome) > 3:
        nome = int(input("digite sua idade"))

idade = int(input("Digite uma idade entre 0 e 150: "))
salario = int(input("Digite um salario mair que 0: "))
sexo = (input("Digite um sexo m ou f: "))
estado_civil = (input("digite o estado civil s,c,v,d: "))

print(idade)
print(salario)
print(sexo)
print(estado_civil)
    

