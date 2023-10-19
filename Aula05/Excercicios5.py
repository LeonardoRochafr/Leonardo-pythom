
A = 80000
taxa_a = float(input("digite a taxa de crescimento para país A"))
B = 200000
taxa_b = float(input("digite a taxa de crescimento para o país B"))

anos = 0

while A < B:
    A += A * taxa_a
    B += B * taxa_b
    
    anos += 1
print(" o Pais A levara ", anos," anos para ultrapassar o país B")

