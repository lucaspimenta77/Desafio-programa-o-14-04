numero = int(input("Digite um número de 4 dígitos: "))
if numero < 999:
    print("Digite novamente! O numero nao tem 4 digitos!")

# Separa o número em duas partes de dois dígitos
parte1 = numero // 100
parte2 = numero % 100

# Soma as partes e verifica se o quadrado é igual ao número original
if (parte1 + parte2) ** 2 == numero:
    print(numero, "obedece a característica.")
else:
    print(numero, "não obedece a característica.")
