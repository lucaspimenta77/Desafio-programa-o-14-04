#Fazer um algoritmo que calcule e escreva o somatório dos valores armazenados numa variável composta unidimensional (vetor) A, de 100 elementos numéricos a serem lidos do dispositivo de entrada.

vetor = []

for i in range(5):
    elemento = int(input(f'Digite o valor do elemento{i+1}: '))
    vetor.append(elemento)

soma = 0
for elemento in vetor:
    soma += elemento

print('O somatorio dos elementos é', soma)