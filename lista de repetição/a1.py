soma = 0
count = 0
negativos = []

i = 0
while i < 20:
    num = int(input("Digite um número inteiro: "))

    if num < 0:
        negativos.append(num)
    else:
        soma += num
        count += 1

    i += 1

if len(negativos) > 0:
    print("Números negativos:", negativos)

if count > 0:
    media = soma / count
    print("Média dos números positivos:", media)
else:
    print("Não foram digitados números positivos.")
