#Faça um algoritmo que leia um vetor que contém as notas de 30 alunos. Imprima o maior valor, o menor valor, a média da turma e a quantidade de notas abaixo da média.

Vetor = []

for i in range(30):
    aluno = float(input('Digite a nota do aluno{}:'.format(i+1)))
    Vetor.append(aluno)


maior = max(Vetor)

menor = min(Vetor)

soma = sum(Vetor)
media = soma / len(Vetor)

abaixo_media = 0
for aluno in Vetor:
    if aluno < media:
        abaixo_media += 1
print("Maior valor:", maior)
print("Menor valor:", menor)
print("Média da turma:", media)
print("Quantidade de notas abaixo da média:", abaixo_media)
