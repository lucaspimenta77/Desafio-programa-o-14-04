n = int(input("Digite a quantidade de valores a serem lidos: "))
contador_negativos = 0

for i in range(n):
    valor = int(input(f"Digite o valor {i+1}: "))
    if valor < 0:
        contador_negativos += 1

print("A quantidade de valores negativos é:", contador_negativos)
