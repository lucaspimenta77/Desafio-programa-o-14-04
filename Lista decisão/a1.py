numero = int(input("Digite um número: "))
if (numero >= 20) and (numero <= 90):
    print("Numero no intervalo [20,90]")
else:
    print("Numero fora do intervalo [20,90]")

a = int(input("Entre com o primeiro número: "))
b = int(input("Entre com o segundo número: "))
c = int(input("Entre com o terceiro número: "))

if not (c > 5):
    d = (a + b) * c
else:
    d = (a - b) * c

print(d)
