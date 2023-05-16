def calcular_quilometragem(odometro_anterior, odometro_atual, quantidade_combustivel):
    distancia_percorrida = odometro_atual - odometro_anterior
    quilometragem_por_litro = distancia_percorrida / quantidade_combustivel
    return quilometragem_por_litro


numero_reabastecimentos = int(input("Digite o número total de reabastecimentos: "))

quilometragem_total = 0
combustivel_total = 0

for i in range(numero_reabastecimentos):
    odometro = float(input(f"Digite o odômetro na parada {i + 1}: "))
    quantidade_combustivel = float(
        input(f"Digite a quantidade de combustível na parada {i + 1}: ")
    )

    if i == 0:
        odometro_inicial = odometro
        combustivel_inicial = quantidade_combustivel
    else:
        quilometragem_por_litro = calcular_quilometragem(
            odometro_anterior, odometro, quantidade_combustivel
        )
        print(
            f"A quilometragem obtida por litro entre as paradas {i} e {i + 1} é: {quilometragem_por_litro:.2f}"
        )

    quilometragem_total += odometro - odometro_inicial
    combustivel_total += quantidade_combustivel
    odometro_anterior = odometro

quilometragem_media = quilometragem_total / combustivel_total
print(
    f"A quilometragem média obtida por litro em toda a viagem é: {quilometragem_media:.2f}"
)
