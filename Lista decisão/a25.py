# Escrever um algoritmo para ler dois valores e uma das seguintes operações a serem executadas (codificadas da seguinte forma: 1 – Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão). Calcular e escrever o resultado dessa operação sobre os dois valores lidos.

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
forma = int(input("Digite a operação que deseja realizar(1 - adição 2 - subtração  3- Multiplicação  4 - divisão): "))
if forma == 1:
    resultado = valor1 + valor2
elif forma == 2:
    resultado = valor1 - valor2
elif forma == 3:
    resultado = valor1 * valor2
elif forma == 4:
    resultado = valor1 / valor2
else:
    print("Opção inválida")
    resultado = None

if resultado is not None:
    print(f"O resultado é: {resultado}")
