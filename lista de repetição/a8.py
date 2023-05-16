n = int(input("Digite a quantidade de atletas: "))

maior_altura = 0
maior_inscricao = 0
menor_altura = float('inf')
menor_inscricao = 0
soma_alturas = 0

for i in range(n):
    inscricao = int(input("Digite o número de inscrição do atleta: "))
    altura = float(input("Digite a altura do atleta (em cm): "))

    if altura > maior_altura:
        maior_altura = altura
        maior_inscricao = inscricao

    if altura < menor_altura:
        menor_altura = altura
        menor_inscricao = inscricao

    soma_alturas += altura

media_alturas = soma_alturas / n

print("Atleta mais alto:")
print("Número de inscrição:", maior_inscricao)
print("Altura:", maior_altura, "cm")

print("\nAtleta mais baixo:")
print("Número de inscrição:", menor_inscricao)
print("Altura:", menor_altura, "cm")

print("\nAltura média do grupo:", media_alturas, "cm")
