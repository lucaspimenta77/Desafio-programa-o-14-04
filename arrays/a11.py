#11) Faça um algoritmo que leia um conjunto de 10 elementos reais e os coloque em um vetor.
#Construa um segundo vetor formado da seguinte maneira:
#• Os elementos de ordem par são os correspondentes do primeiro vetor multiplicados por 3.
#• Os elementos de ordem ímpar são os correspondentes do primeiro vetor divididos por 2.
#• Imprima os dois vetores.

vetor = []
vetor2 = []

for i in range(10):
    vetor.append(float(input(f'Digite o {i+1}o valor: ')))

for i in range(10):
    if i % 2 == 00:
        vetor2.append(vetor[i] * 3)
    else:
        vetor2.append(vetor[i] / 2)

print('Primeiro vetor', vetor)
print('Segundo vetor', vetor2)