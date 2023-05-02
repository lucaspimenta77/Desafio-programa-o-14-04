#Ler um valor e escrever a mensagem É MAIOR QUE 10! se o valor lido for maior que 10, caso contrário escrever NÃO É MAIOR QUE 10!

p1 = float(input('Digite um valor: '))

if(p1 >= 11):
    print('É MAIOR QUE 10!')
elif(p1 == 10):
    print('SEU VALOR É 10!')    
else:
    print('NÃO É MAIOR QUE 10!')