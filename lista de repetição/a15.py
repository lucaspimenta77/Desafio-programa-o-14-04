

soma = 0

for i in range(20):
    numerador = 100 - i
    fatorial = 1

    for j in range(i + 1):
        if j > 0:
            fatorial *= j

    termo = numerador / fatorial
    soma += termo

print("A soma dos 20 primeiros termos da série é:", soma)
