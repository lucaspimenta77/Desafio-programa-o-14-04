#Escreva um algoritmo que leia um conjunto de 10 notas, armazene-as em uma variável composta chamada NOTA e calcule e imprima a sua média.

Nota  = []

for i in range(10):
    nota = float(input('Digite a nota{}: '.format(i+1)))
    Nota.append(nota)

soma = sum(Nota)
media = soma / len(Nota)

print('A media das notas é:', media)


