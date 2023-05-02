#Escreva um algoritmo que leia 4 valores (opção, a, b, c), onde opção é um valor inteiro e positivo e a, b, c são quaisquer valores reais. Escreva os valores lidos da seguinte maneira:
#se opção = 1 Þ escreva os 3 valores a, b, c em ordem crescente
#se opção = 2 Þ escreva os 3 valores a, b, c em ordem decrescente
#se opção = 3 Þ escreva os 3 valores de forma que o maior valor entre a, b, c fica entre os outros 2.


opcao = int(input("Digite a opção desejada (1(ordem crescente), 2(ordem decrescente) ou 3(maior valor entre a, b, c fica entre os outros 2)): "))
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if opcao == 1:
    valores_ordenados = sorted([a, b, c])
    print(f"Os valores em ordem crescente são: {valores_ordenados[0]}, {valores_ordenados[1]} e {valores_ordenados[2]}")


elif opcao == 2:
    valores_ordenados = sorted([a, b, c], reverse=True)
    print(f"Os valores em ordem decrescente são: {valores_ordenados[0]}, {valores_ordenados[1]} e {valores_ordenados[2]}")


elif opcao == 3:
    valores = [a, b, c]
    maior_valor = max(valores)
    valores.remove(maior_valor)
    valores_ordenados = sorted(valores)
    print(f"Os valores com o maior no meio são: {valores_ordenados[0]}, {maior_valor} e {valores_ordenados[1]}")


else:
    print("Opção inválida. Digite 1, 2 ou 3.")
