#Faça um algoritmo que leia 3 valores a, b, c, e verifique se podem ser os comprimentos dos lados de um triângulo. Em caso afirmativo, verifique se é “triângulo equilátero”, “triângulo isósceles” ou “triângulo escaleno”. Em caso negativo, escreva uma mensagem: “os valores lidos não formam um triângulo”. Considere que:
#• o comprimento de cada lado de um triângulo é menor que a soma dos comprimentos dos outros lados
#• um triângulo equilátero tem três lados iguais
#• um triângulo isósceles tem dois lados iguais e um diferente

l1 = float(input('digite o primeiro lado'))
l2 = float(input('digite o 2 lado'))
l3 = float(input('digite o terceiro lado'))


if (l1 == l2 and l2 == l3):
    print('Equilatero')

elif (l1 == l2 or l1 == l3 or l2 == l3):
    print('isosceles')
else:
    print('escaleno')
