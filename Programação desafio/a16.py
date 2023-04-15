#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math
print('Bem vindo a nossa loja!! Nossa loja tem esse programa para o comprador saber quantas latas de tintas deve ser compradas e seu valor!')
metros = float(input('Quantidade a ser pintada em metros quadrados: '))

litros = metros / 3
latas = math.ceil(litros/18)

preço= latas * 80

print(f'Para pintar {metros} metros, voce tera que utilizar {latas} latas de tinta e irá gastar {preço}R$ ')
