# Faça um algoritmo que leia as 3 notas de um aluno e calcule e escreva a média final deste aluno. Considerar que a média é ponderada e que o peso das notas é: 2,3 e 5, respectivamente.


n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = float(input('Digite sua terceira nota: '))

p1 = n1 * 0.2
p2 = n2 * 0.3
p3 = n3 * 0.5
media = (p1 + p2 + p3)

print(f'Sua media final é {media}')
