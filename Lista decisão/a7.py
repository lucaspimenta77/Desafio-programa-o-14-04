#Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).

ano_atual = int(input('Digite o ano atual: '))
nascimento = int(input('Digite seu ano de nascimento: '))

idade = ano_atual - nascimento

if idade >= 18:
    print('Você poderá votar este ano.')
elif idade == 16 or idade == 17:
    print('Você não é obrigada a votar, mas pode votar. ')
else:
    print('Você nao poderá votar este ano.')