import math

massa_inicial = float(input("Digite a massa inicial do material em Kg: "))
massa_final = 0.5 / 1000  # Convertendo para Kg
tempo_meia_vida = 50  # segundos

tempo = tempo_meia_vida * math.log(massa_final / massa_inicial) / math.log(0.5)

print("Massa inicial:", massa_inicial, "Kg")
print("Massa final:", massa_final, "Kg")
print("Tempo necessário:", tempo, "segundos")
