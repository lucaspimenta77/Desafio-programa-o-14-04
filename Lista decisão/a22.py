#Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos 2 maiores.
entrada = input("Digite três valores separados por um espaço: ")


valores = entrada.split()


valores = [int(valor) for valor in valores]


if valores[0] != valores[1] != valores[2]:

    valores_ordenados = sorted(valores)
    v = valores_ordenados[1] + valores_ordenados[2]
    print(f" A soma dos dois maiores valores é: {v}")

else:
   
    print("Os valores são iguais. Digite valores diferentes.")