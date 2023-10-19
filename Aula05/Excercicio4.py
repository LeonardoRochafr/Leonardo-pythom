
A = 80000
taxa_a = 0.03
B = 200000
taxa_b = 0.015

anos = 0

while A < B:
    A += A * taxa_a
    B += B * taxa_b
    
    anos += 1
print(" o Pais A levara ", anos,"para ultrapassar o país B")

