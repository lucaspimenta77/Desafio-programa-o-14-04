#Entrar com um número e informar se ele é divisível por 5.

valor = int(input('Digite o valor: '))

if valor % 5 == 0:
    print(f"O número {valor} é divisível por 5")
else:
    print(f"O número {valor} não é divisível por 5")
