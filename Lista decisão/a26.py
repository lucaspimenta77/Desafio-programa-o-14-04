#Faça um algoritmo para calcular as raízes reais de uma equação quadrática: ax2 + bx + c = 0. Uma equação quadrática só tem raiz reais se (b2 - 4ac) for maior ou igual a zero. O algoritmo deverá informar as seguintes situações:
#• Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa;
#• Se o delta calculado for igual a zero a equação possui apenas uma raiz real, informe-a ao usuário;
#• Se o delta for positivo, a equação possui duas raiz reais, informe-as ao usuário.

import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("A equação não possui raízes reais.")
elif delta == 0:
    x = -b / (2*a)
    print(f"A equação possui apenas uma raiz real: x = {x}")
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"A equação possui duas raízes reais: x1 = {x1} e x2 = {x2}")
