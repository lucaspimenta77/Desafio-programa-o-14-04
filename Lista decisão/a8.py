#Entrar com o ano de nascimento de uma pessoa e imprimir a idade dela. Verificar se o ano digitado é válido.

ano_atual = 2023

digitar_ano = int(input('Digite o ano de seu nascimento: '))

ano = ano_atual - digitar_ano

if digitar_ano > ano_atual:
    print('O ano digitado é maior que o ano atual.')

else:
    print(f'Sua idade é {ano} anos!')