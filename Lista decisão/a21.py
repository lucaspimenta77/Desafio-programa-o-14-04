#Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles.
entrada = input("Digite três valores separados por um espaço: ")


valores = entrada.split()


valores = [int(valor) for valor in valores]


if valores[0] != valores[1] != valores[2]:

    valores_ordenados = sorted(valores)
    print(f"O maior valor é {valores_ordenados[2]}")

else:
   
    print("Os valores são iguais. Digite valores diferentes.")