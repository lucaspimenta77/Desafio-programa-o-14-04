n = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é válido
if n < 0:
    print("O número precisa ser positivo.")
else:
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    print("O fatorial de", n, "é:", fatorial)
