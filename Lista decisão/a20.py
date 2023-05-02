
entrada = input("Digite dois valores separados por um espaço: ")


valores = entrada.split()


valores = [int(valor) for valor in valores]


if valores[0] != valores[1]:

    valores_ordenados = sorted(valores)
    print(f"Os valores em ordem crescente são: {valores_ordenados[0]} e {valores_ordenados[1]}")

else:
   
    print("Os valores são iguais. Digite dois valores diferentes.")