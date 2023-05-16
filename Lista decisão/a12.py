#Escrever um algoritmo para ler a quantidade de horas aula dadas por dois professores e o valor por hora recebido por cada um. Mostrar na tela qual dos professores tem salário total maior.

horas_aula1 = int(input("Digite a quantidade de horas aula do primeiro professor: "))
valor_hora1 = float(input("Digite o valor por hora do primeiro professor: "))
salario1 = horas_aula1 * valor_hora1

horas_aula2 = int(input("Digite a quantidade de horas aula do segundo professor: "))
valor_hora2 = float(input("Digite o valor por hora do segundo professor: "))
salario2 = horas_aula2 * valor_hora2

if salario1 > salario2:
    print("O primeiro professor tem salário total maior.")
else:
    print("O segundo professor tem salário total maior.")







