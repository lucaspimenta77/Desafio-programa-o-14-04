#Escreva um algoritmo que leia um vetor de 200 valores numéricos reais e os imprima na ordem contrária em que foi lida.
vetor = []

for i in range(5):
    elementos = int(input(f'Digite o valor dos elementos{i+1}: '))
    vetor.append(elementos)

for elemento in reversed(vetor):
    print(elemento)