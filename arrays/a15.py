#15) Classificar um vetor numérico VET de 20 elementos em ordem crescente.

Vet = []

for i in range(20):
    Vet.append(float(input(f'Digite o valor {i+1} do vetor: ')))

vetor = sorted(Vet)

print(vetor)