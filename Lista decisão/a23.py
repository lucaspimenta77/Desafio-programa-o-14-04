#Ler 3 valores (considere que não serão informados valores iguais) e escrevê-los em ordem crescente.

entrada = input("Digite três valores separados por um espaço: ")


valores = entrada.split()


valores = [int(valor) for valor in valores]


if valores[0] != valores[1] != valores[2]:

    valores_ordenados = sorted(valores)
    print(f"Os valores em ordem crescente são: {valores_ordenados[0]}, {valores_ordenados[1]} e {valores_ordenados[2]}")

else:
   
    print("Os valores são iguais. Digite valores diferentes.")