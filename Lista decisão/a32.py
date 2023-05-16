valor = int(input("Digite um valor de 1 a 4: "))
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if valor == 0:
    resultado = num1 + num2
    print(f"A soma dos números é: {resultado}")
    
elif valor == 1:
    resultado = num1 - num2
    print(f"A subtração dos números é: {resultado}")
    
elif valor == 2:
    resultado = num1 * num2
    print(f"A multiplicação dos números é: {resultado}")
    
elif valor == 3:
    resultado = num1 / num2
    print(f"A divisão dos números é: {resultado}")
    
elif valor == 4:
    resultado = (num1 + num2) / 2
    print(f"A média dos números é: {resultado}")
    
else:
    print("Valor errado. Programa encerrado sem cálculos")