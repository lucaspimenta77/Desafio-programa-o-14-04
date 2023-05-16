soma_pares = 0
soma_impares = 0

for i in range(1, 101):
    if i % 2 == 0:
        soma_pares += i
    else:
        soma_impares += i

print("A soma dos números pares entre 1 e 100 é:", soma_pares)
print("A soma dos números ímpares entre 1 e 100 é:", soma_impares)
