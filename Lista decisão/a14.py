#Ler o nome de 2 times e o número de gols marcados na partida. Escrever o nome do vencedor. Caso não haja vencedor deverá ser impressa a palavra EMPATE.

t1 = str(input('Digite o nome do time da casa: '))
g1 = int(input('Quantos gols esse time marcou? '))
t2 = str(input('Digite o nome do time visitante: '))
g2 = int(input('Quantos gols esse time marcou? '))

if g1 > g2:
    print(f'O {t1} foi o time vencedor')

elif g1 < g2:
    print(f'O {t2} foi o time vencedor')
    
else:
    print(f'A partida entre {t1} e {t2} acabou em empate!')