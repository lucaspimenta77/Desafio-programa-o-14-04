a = float(input('Insire o valor de a: '))
b = float(input('Insire o valor de b: '))
c = float(input('Insire o valor de c: '))
d = float(input('Insire o valor de d: '))
e = float(input('Insire o valor de e: '))
f = float(input('Insire o valor de f: '))

x = (c * e - b * f) / (a * e - b * d)
y = (a * f - c * d) / (a * e - b * d)

print(f'Os valores de x e y são: x={x} e y={y}')
