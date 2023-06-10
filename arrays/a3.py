#Repita o algoritmo acima, porém imprima quantos valores estão acima da média.

Nota  = []

for i in range(10):
    nota = float(input('Digite a nota{}: '.format(i+1)))
    Nota.append(nota)

soma = sum(Nota)
media = soma / len(Nota)

print('A media das notas é:', media)

acima_media = 0
for nota in Nota:
    if nota > 5.9:
        acima_media += 1
print("Quantidade de notas acima da média:", acima_media)
