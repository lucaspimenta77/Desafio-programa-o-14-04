

d = float(input('Digite a distancia em KM: '))
consumo = float(input('Digite a media de  KM por litro o carro faz: '))
preco = float(input('Digite o preço da gasolina em sua região: R$ '))
litros = d/consumo
valor = litros * preco

print(f'Para percorrer a distancia de {d}Km voce tera que por um total de {litros} litros de gasolina e gastar um total de {preco}R$')
