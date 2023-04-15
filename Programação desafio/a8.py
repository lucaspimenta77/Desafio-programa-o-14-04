#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

print('Bem vindo, iremos calcular o salario que sua pessoa irá receber esse mes')
a1= float(input('Nos diga quantos R$ recebe por hora: R$'))
a2= int(input('Quantas horas você trabalha por dia?: '))
a3 = int(input('Agora diga quantos dias por mês voce trabalha: '))
a4 = (a1 * a2) * a3
print(f'O seu salario mensal será de {a4}R$')