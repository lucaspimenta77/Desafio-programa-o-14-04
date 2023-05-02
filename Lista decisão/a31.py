temperatura = int(input('Digite a temperautra desejada: °C  '))

if temperatura <= 500:
    print("Temperatura Inválida")
elif temperatura < 700:
    print("Aquecimento Ligado em 100%")
elif temperatura < 735:
    print("Aquecimento Ligado em 50%")
elif temperatura >= 735 and temperatura <= 780:
    print("Aquecimento Desligado")
elif temperatura >= 1000:
    print("Temperatura Inválida")
else:
    print("Superaquecimento")

