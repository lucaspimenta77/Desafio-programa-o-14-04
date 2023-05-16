n = int(input("Digite a quantidade de pessoas: "))
soma_altura_mulheres = 0
contador_mulheres = 0
soma_altura_turma = 0

for i in range(n):
    altura = float(input("Digite a altura da pessoa em cm: "))
    sexo = input("Digite o sexo da pessoa (M/F): ")

    if sexo.upper() == 'F':
        soma_altura_mulheres += altura
        contador_mulheres += 1

    soma_altura_turma += altura

media_altura_mulheres = soma_altura_mulheres / contador_mulheres
media_altura_turma = soma_altura_turma / n

print("Média da altura das mulheres:", media_altura_mulheres)
print("Média da altura da turma:", media_altura_turma)
