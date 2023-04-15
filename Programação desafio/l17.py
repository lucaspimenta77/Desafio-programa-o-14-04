#Faça um algoritmo que leia o salário bruto mensal de um funcionário, calcule e
#mostre os valores conforme modelo abaixo:
#Salário Bruto :R$
#(-) IR (15%) :R$
#(-) INSS (11%) :R$
#(-) Sindicato (3%) :R$
#Salário Líquido :R$


print('Bem vindo, iremos calcular o salario que sua pessoa irá receber esse mes')
a1= float(input('Nos diga quantos R$ recebe por hora: R$'))
a2= int(input('Quantas horas você trabalha por dia?: '))
a3 = int(input('Agora diga quantos dias por mês voce trabalha: '))
a4 = (a1 * a2) * a3
print(f'O seu salario mensal será de {a4}R$ que é seu salario bruto.')

print('Porem temos que lembrar que são descontado 15% para o imposto de renda, 11% para o INSS e 3% para o sindicato. ')


inss = a4 * 0.11

s = a4 * 0.03

renda = a4 * 0.15
desconto = inss + s + renda
liquido = a4 - desconto
print(f'Pagou ao INSS {inss}R$')
print(f'Pagou ao sindicato {s}R$')
print(f'Pagou ao imposto de renda {renda}R$')
print(f'O seu salario liquido é de {liquido}R$')