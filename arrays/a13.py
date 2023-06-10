#13) Escreva um algoritmo que:
#a) leia uma frase de 50 caracteres;
#b) conte quantos brancos existem na frase;
#c) conte quantas vezes a letra “A” aparece;
#d) imprima o que foi calculado nos itens b e c.

# Passo 1: Ler a frase de 50 caracteres
frase = input("Digite uma frase de 50 caracteres: ")

# Passo 2: Contar os espaços em branco na frase
contador_brancos = 0
for caractere in frase:
    if caractere == ' ':
        contador_brancos += 1

# Passo 3: Contar a quantidade de vezes que a letra "A" aparece na frase
contador_A = 0
for caractere in frase:
    if caractere == 'A' or caractere == 'a':  # considerando tanto "A" maiúsculo quanto "a" minúsculo
        contador_A += 1

# Passo 4: Imprimir os resultados
print("Quantidade de espaços em branco na frase:", contador_brancos)
print("Quantidade de vezes que a letra 'A' aparece na frase:", contador_A)
