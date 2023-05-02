# Entrar com um número de 1 a 12 e exibir o mês correspondente.

import calendar

mes = int(input('Digite um número de 1 a 12: '))

if 1 <= mes <= 12:
    nome_mes = calendar.month_name[mes]
    print(nome_mes)
else:
    print('Número inválido de mês')