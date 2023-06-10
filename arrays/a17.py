# Passo 1: Ler o vetor de 128 elementos
vetor = []
for _ in range(5):
    elemento = int(input("Digite um elemento do vetor: "))
    vetor.append(elemento)

# Passo 2: Ler a chave K
chave = int(input("Digite a chave: "))

# Passo 3: Pesquisa Binária para verificar se a chave existe no vetor
encontrada = False
inicio = 0
fim = 4

while inicio <= fim:
    meio = (inicio + fim) // 2  # Encontra o elemento do meio

    if vetor[meio] == chave:
        encontrada = True
        posicao = meio
        break
    elif vetor[meio] < chave:
        inicio = meio + 1
    else:
        fim = meio - 1

# Passo 4: Imprimir a posição onde a chave foi encontrada ou a mensagem de chave não encontrada
if encontrada:
    print("A chave", chave, "foi encontrada na posição", posicao)
else:
    print("CHAVE", chave, "NÃO ENCONTRADA")
