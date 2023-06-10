#Dado um vetor de 128 elementos, verificar se existe um elemento igual a K (chave) no vetor. Se existir, imprimir a posição onde foi encontrada a chave; se não; imprimir a mensagem: “CHAVE K NÃO ENCONTRADA”. O vetor A e a chave K são lidos a partir de uma unidade de entrada.

vetor = []

for i in range (5):
    vetor.append(float(input('Digite o elemento do vetor: ')))

chave = int(input('Digite a chave: '))

encontrada = False
posicao = -1
for i in range(5):
    if vetor[i] == chave:
        encontrada = True
        posicao = i
        break

if encontrada:
    print("A chave", chave, "foi encontrada na posição", posicao)
else:
    print("CHAVE", chave, "NÃO ENCONTRADA")