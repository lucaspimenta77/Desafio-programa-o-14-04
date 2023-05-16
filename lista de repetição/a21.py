quantidade_alunos = 50
alunos_18_anos = []
quantidade_alunos_acima_20_anos = 0

for i in range(quantidade_alunos):
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))

    if idade == 18:
        alunos_18_anos.append(nome)

    if idade > 20:
        quantidade_alunos_acima_20_anos += 1

print("Alunos com 18 anos:")
for aluno in alunos_18_anos:
    print(aluno)

print("Quantidade de alunos acima de 20 anos:", quantidade_alunos_acima_20_anos)
