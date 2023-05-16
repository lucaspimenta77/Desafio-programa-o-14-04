#Entrar com a idade de uma pessoa e exibir a mensagem; Maior de idade, menor de idade ou acima de 65 anos.

idade = int(input('Digite sua idade: '))

if idade >= 18 and idade < 65:
    print('Você é maior de idade.')
elif idade >= 65:
    print('Você tem acima de 65 anos.')
elif idade < 0:
    print('Sua idade é invalida.')
else:
    print('Você é menor de idade.')
