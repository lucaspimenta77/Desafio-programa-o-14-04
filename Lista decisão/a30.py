#Faça um algoritmo para calcular o reajuste salarial de um funcionário, de acordo com os critérios abaixo:
#• se salário é inferior a R$ 10.000,00 deve ter um reajuste de 55%
#• se salário está entre R$ 10.000,00 (inclusive) e R$ 25.000,00 (inclusive) deve ter um reajuste de 20%
#• se salário é superior a R$ 25.000,00 deve ter um reajuste de 20%.
salario_atual = float(input("Digite o salário atual do funcionário: "))

if salario_atual < 10000:
    aumento = 0.55
elif salario_atual <= 25000:
    aumento = 0.20
elif salario_atual > 25000:
    aumento = 0.20

    
salario_corrigido = salario_atual * (1 + aumento)

if aumento > 0:
    print(f"O funcionário terá um aumento de {aumento*100}% e seu salário corrigido será de R$ {salario_corrigido}.")
else:
    print("O funcionário não terá aumento salarial.")