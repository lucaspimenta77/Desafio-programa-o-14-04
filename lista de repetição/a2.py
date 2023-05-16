# Faça um algoritmo que leia 15 números inteiros e escreva, para cada número lido, se é par ou ímpar.

for i in range(1, 16):
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        print("O número", num, "é par.")
    else:
        print("O número", num, "é ímpar.")
