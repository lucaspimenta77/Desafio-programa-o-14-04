# Ler um vetor de 100 elementos numéricos e verificar se existem elementos iguais a 30. Se existirem, escrever as posições em que estão armazenados.

Vetor = []
posicoes_iguais_a_30 = []

for i in range(5):
    elemento = int(input(f"Digite o valor numero{i+1}: "))
    Vetor.append(elemento)

for i in range(5):
    if Vetor[i] == 30:
        posicoes_iguais_a_30.append(i)

if len(posicoes_iguais_a_30) > 0:
    print("Elementos iguais a 30 encontrados nas posições:")
    for posicao in posicoes_iguais_a_30:
        print(posicao)
else:
    print("Nenhum elemento igual a 30 encontrado.")
