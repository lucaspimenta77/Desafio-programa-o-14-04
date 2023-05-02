#Escrever um algoritmo para ler duas notas de um aluno e escrever na tela a palavra “Aprovado” se a média das duas notas for maior ou igual a 7,0. Caso a média seja inferior a 7,0, o programa deve ler a nota do exame e calcular a média final. Se esta média for maior ou igual a 5,0, o programa deve escrever “Aprovado”, caso contrário deve escrever “Reprovado”.

n1 = float(input('Digite a nota da primeira avaliação: '))
n2= float(input('Digite a nota da segunda avaliação: '))

nf = (n1 + n2) / 2

if nf >= 7:
    print('Aprovado!')
else:
    nota_exame = float(input("Digite a nota do exame: "))
    media_final = (nf + nota_exame) / 2
    if media_final >= 5.0:
        print("Aprovado")
    else:
        print("Reprovado")