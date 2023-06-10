#Fazer um algoritmo que:
#a) Leia duas variáveis compostas unidimensionais, contendo, cada uma, 25 elementos numéricos;
#b) intercale os elementos desses dois conjuntos formando uma nova variável composta unidimensional de 50 elementos;
#c) Escreva o resultado obtido.

vetor = []
vetor2 = []

for i in range(10):
    vetor.append(int(input(f'Digite o valor{i+1} do primeiro vetor: ')))

for i in range(10):
    vetor2.append(int(input(f'Digite o valor{i+1} do segundo vetor: ')))

variavel = []

for vetor, vetor2 in zip(vetor , vetor2):
    variavel.append(vetor)
    variavel.append(vetor2)

print(variavel)