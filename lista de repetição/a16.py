import math

def calcular_fatorial(n):
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial

x = float(input("Digite o valor de x: "))

resultado_ex = 0
for i in range(30):
    termo = math.pow(x, i) / calcular_fatorial(i)
    resultado_ex += termo

print("O valor de e^x é:", resultado_ex)
