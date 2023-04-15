#Faça um algoritmo que leia as coordenadas de dois pontos, P1 (x1, y1) e P2 (x2, y2) respectivamente, e calcule e escreva a distância entre eles.
import math
x1 = float(input('Digite a coordenada de x no P1: '))
y1 = float(input('Digite a coordenada de y no P1: '))
x2 = float(input('Digite a coordenada de x no P2: '))
y2 = float(input('Digite a coordenada de y no P2: '))

distancia = math.sqrt((x2-x1)**2+(y2-y2)**2)
print(f'A distancia entre o ponto P1({x1}, {y1}) e P2 ({x2}, {y2}) é de {distancia}')