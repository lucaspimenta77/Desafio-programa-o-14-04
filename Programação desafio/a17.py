#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

#comprar apenas latas de 18 litros; 
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre
#arredonde os valores para cima, isto é, considere latas cheias.

import math


area = float(input("Quantidade a ser pintada em metros quadrados: "))


litrostinta = area / 6 * 1.1


quantidadelatas = math.ceil(litrostinta / 18)


quantidadegaloes = math.ceil(litrostinta / 3.6)

precototallatas = quantidadelatas * 80


precototalgaloes = quantidadegaloes * 25


quantidade_latas_misturadas = quantidadelatas
quantidade_galoes_misturados = 0
while (quantidade_latas_misturadas * 18 - litrostinta) < 0:
    quantidade_galoes_misturados += 1
    quantidade_latas_misturadas = math.ceil((litrostinta - quantidade_galoes_misturados * 3.6) / 18)
preco_total_misturado = quantidade_latas_misturadas * 80 + quantidade_galoes_misturados * 25

print(f"Quantidade de latas de tinta a serem compradas: {quantidadelatas}")
print(f"Preço total comprando apenas latas de 18 litros: R${precototallatas:}")
print(f"Quantidade de galões de tinta a serem comprados: {quantidadegaloes}")
print(f"Preço total comprando apenas galões de 3,6 litros: R${precototalgaloes:}")
print(f"Quantidade de galões de tinta a serem comprados: {quantidade_galoes_misturados}")
print(f"Quantidade de latas de tinta a serem compradas: {quantidade_latas_misturadas}")
print(f"Preço total misturando latas e galões: R${preco_total_misturado}")