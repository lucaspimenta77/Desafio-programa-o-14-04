salario_atual = float(input("Digite o salário atual do funcionário: "))

if salario_atual <= 400:
    aumento = 0.15
elif salario_atual <= 700:
    aumento = 0.12
elif salario_atual <= 1000:
    aumento = 0.1
elif salario_atual <= 1500:
    aumento = 0.07
elif salario_atual <= 2000:
    aumento = 0.04
else:
    aumento = 0
    
salario_corrigido = salario_atual * (1 + aumento)

if aumento > 0:
    print(f"O funcionário terá um aumento de {aumento*100}% e seu salário corrigido será de R$ {salario_corrigido}.")
else:
    print("O funcionário não terá aumento salarial.")
