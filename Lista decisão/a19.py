#Ler 2 valores (considere que não serão lidos valores iguais) e escrever o maior deles.

v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))

if v1 > v2:
    print(f'O primeiro valor cujo é {v1} é o maior valor.')
elif v2 > v1:
    print(f'O segundo valor cujo é {v2} é o maior valor.')

else:
    print ('Valor invalido.')