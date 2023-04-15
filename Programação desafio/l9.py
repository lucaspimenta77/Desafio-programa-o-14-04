#Faça um algoritmo que calcule o volume de uma lata de óleo. Escreva o resultado. 
#FÓRMULA: volume = p * raio2 * altura
import math
pi = math.pi
a1= float(input('Digite a altura da lata: '))
a2= float(input("Digite o Raio da lata: "))

a3 = pi * (a2**2) * a1

print(f'O volume da lata é {a3}')