#Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o valor da compra for menor que R$ 20,00; Caso contrário, o lucro será de 30%. Entrar com o valor do produto e imprimir o valor da venda.

p1 = float(input('Qual o valor original do produto: R$ '))
 
if p1 >= 20:
    p2 = p1 * 0.45
    p3 = p1 + p2
    print(f'O valor a ser vendido vai ser de R${p3}')
else:
    p4 = p1 * 0.30
    p5 = p1 + p4
    print(f'O valor a ser vendido vai ser de R$ {p5}')