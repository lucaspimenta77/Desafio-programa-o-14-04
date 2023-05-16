audiencia_total = {"4": 0, "5": 0, "9": 0, "12": 0}

n = int(input("Digite o número de casas visitadas: "))

for i in range(n):
    canal = input("Digite o número do canal (4, 5, 9, 12): ")
    audiencia = int(input("Digite o número de pessoas assistindo: "))

    audiencia_total[canal] += audiencia

total_audiencia = sum(audiencia_total.values())

print("Percentual de audiência por emissora:")
for canal, audiencia in audiencia_total.items():
    percentual = (audiencia / total_audiencia) * 100
    print(f"Canal {canal}: {percentual:.2f}%")
