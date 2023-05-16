numero = int(input("Digite um número inteiro: "))

divisores = []
quantidade_divisores = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores.append(i)
        quantidade_divisores += 1

print(f"Número lido: {numero}")
print("Divisores:", end=" ")
for divisor in divisores:
    print(divisor, end=" ")
    
print("\nQuantidade de divisores:", quantidade_divisores)
