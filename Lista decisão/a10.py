#Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que se a nota for igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.

n1 = float(input('Digite a nota da primeira avaliação: '))
n2= float(input('Digite a nota da segunda avaliação: '))

nf = (n1 + n2) / 2

if nf >= 6:
    print('Aprovado!')
else:
    print('Não aprovado!')