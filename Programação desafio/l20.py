

modelo = input('Digite o modelo: ')
marca = input('Digite a marca: ')
ano = int(input('Digite o ano: '))
km_inicial = float(input('Digite o km inicial: '))
km_final = float(input('Digite o km final: '))
litros_de_combustível_consumidos = float(
    input('Digite o litros de combustível consumidos :'))
preço_por_litro = float(input('Digite o preço por litro: R$'))

distancia_percorrida = km_final - km_inicial
consumo = distancia_percorrida / litros_de_combustível_consumidos
total = litros_de_combustível_consumidos * preço_por_litro

print(f"Modelo: {modelo:25} Marca: {marca:15} Ano: {ano}")
print(f"Distância percorrida: {distancia_percorrida} km")
print(
    f"Litros de combustível consumidos: {litros_de_combustível_consumidos} litros")
print(f"Preço por litro: R$ {preço_por_litro}")
print(f"Total a pagar: R$ {total}")
print(f"Consumo médio: {consumo} km/l")
