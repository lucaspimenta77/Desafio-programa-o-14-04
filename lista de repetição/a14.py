soma = 0

for i in range(51):
    termo = ((-1) ** i) * (1 / ((2 * i + 1) ** 3))
    soma += termo

aprox_pi = (soma * 32) ** (1 / 3)

print("O valor aproximado de π é:", aprox_pi)
