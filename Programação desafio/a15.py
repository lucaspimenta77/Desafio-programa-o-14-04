#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

print('Bem vindo, iremos calcular o salario que sua pessoa irá receber esse mes')
a1= float(input('Nos diga quantos R$ recebe por hora: R$'))
a2= int(input('Quantas horas você trabalha por dia?: '))
a3 = int(input('Agora diga quantos dias por mês voce trabalha: '))
a4 = (a1 * a2) * a3
print(f'O seu salario mensal será de {a4}R$ que é seu salario bruto.')

print('Porem temos que lembrar que são descontado 11% para o imposto de renda, 8% para o INSS e 5% para o sindicato. ')


#b. quanto pagou ao INSS.
inss = a4 * 0.08
#c. quanto pagou ao sindicato.
s = a4 * 0.05
#d. o salário líquido.
renda = a4 * 0.11
desconto = inss + s + renda
liquido = a4 - desconto
print(f'Pagou ao INSS {inss}R$')
print(f'Pagou ao sindicato {s}R$')
print(f'Pagou ao imposto de renda {renda}R$')
print(f'O seu salario liquido é de {liquido}R$')