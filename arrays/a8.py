# Escreva um algoritmo para fazer a soma de dois vetores de 10 elementos reais lidos do teclado. O primeiro elemento do primeiro vetor deverá ser adicionado ao primeiro elemento do segundo vetor e, o resultado deverá ser acumulado em um terceiro vetor também de 10 elementos. Imprimir os três vetores conforme layout de impressão abaixo:

vetor = []
vetor2 = []
vetor3 = []
resultado = []

for i in range(10):
    vetor.append(int(input(f"Digite o valor{i+1} do primeiro vetor: ")))
for i in range(10):
    vetor2.append(int(input(f"Digite o valor{i+1} do segundo vetor: ")))


for i in range(len(vetor)):
    soma = vetor[i] + vetor2[i]
    vetor3.append(soma)

print("vetor: ")
for i in range(10):
    print(f"{vetor[i]}")

print("vetor2:")
for i in range(10):
    print(f"{vetor2[i]}")

print("vetor3")
for i in range(10):
    print(f"{vetor3[i]}")
