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



