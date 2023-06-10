#10) Escreva um algoritmo que:
#a) leia 100 valores numéricos e os armazene numa variável composta unidimensional A;
#b) calcule e escreva:
#c) c) calcule e escreva quantos termos da série acima têm o numerador menor do que o denominador.

a = []


for i in range(5):
    a.append(float(input(f'Digite o valor {i+1} do vetor: ')))

s = 0
contador = 0
for i in range(5):
    termo = i/a[i]
    s += termo
    if i < a[i]:
        contador += 1


print("O valor de S é:", s)
print("O número de termos com numerador menor do que o denominador é:", contador)