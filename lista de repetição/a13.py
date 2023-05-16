N = int(input("Digite o valor de N: "))
soma = 0

for i in range(1, N+1):
    termo = i / (N - i + 1)
    soma += termo

print("O valor de S é:", soma)