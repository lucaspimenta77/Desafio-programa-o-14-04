# Um armazém trabalha com 100 mercadorias diferentes identificadas pelos números inteiros de 0 a 99. O dono do armazém anota a quantidade de cada mercadoria vendida durante o mês. Ele tem uma tabela mensal que indica para cada mercadoria o preço de venda. Escreva o algoritmo para calcular o faturamento mensal do armazém, isto é:


preco = [10, 80, 32, 31, 3]
armazem = [300, 30, 400, 54, 59]

faturamento = 0
for i in range(5):
    faturamento += armazem[i] * preco[i]


print("O faturamento mensal do armazém é:", faturamento, "R$")
