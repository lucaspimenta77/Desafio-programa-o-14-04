# Entrar com a sigla do estado de uma pessoa e imprimir uma das mensagens: “Carioca, Paulista, Mineiro ou Outros”

sigla = {'RJ' :'Carioca', 'SP' : 'Paulista', 'MG' : 'Mineiro'}

s1= str(input('Digite a sigla do seu estado: '))
if s1 in sigla:
    print(sigla[s1])
else:
    print('Outros!')
