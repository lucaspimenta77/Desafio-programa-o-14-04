# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a. o produto do dobro do primeiro com metade do segundo .
# b. a soma do triplo do primeiro com o terceiro.
# c. o terceiro elevado ao cubo.

print('Esse programa irá pedir dois numeros inteiro e um numero real para: A) calcular o o produto do dobro do primeiro com metade do segundo. B)soma do triplo do primeiro com o terceiro. C) terceiro elevado ao cubo.')
n1 = int(input('diga um numero inteiro: '))
n2 = int(input('diga o segundo numero inteiro: '))
n3 = float(input('diga um numero real: '))

a = (n1*2) + (n2/2)
print(f'A) A resposta é: {a}')

b = (n1*3) + n3
print(f'B) A resposta é: {b}')

c = n3**3
print(f'C) A resposta é: {c}')
