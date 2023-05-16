#Dado um conjunto de valores inteiros positivos, determinar qual o menor e qual o maior valor do conjunto. Um número com valor “0” (zero) indica o fim dos dados e não deve ser considerado.


menor = float('inf')
maior = float('-inf')


print("Digite os valores do conjunto (insira 0 para encerrar):")

while True:
    valor = int(input())
    
    if valor == 0:
        break
    
  
    if valor < menor:
        menor = valor
    
   
    if valor > maior:
        maior = valor


if menor == float('inf') or maior == float('-inf'):
    print("Nenhum valor válido foi inserido.")
else:
    print("Menor valor:", menor)
    print("Maior valor:", maior)
