total_pessoas = 20
soma_alturas = 0

for i in range(total_pessoas):
    altura = float(input(f"Informe a altura da pessoa {i+1} em metros: "))
    soma_alturas += altura

media_alturas = soma_alturas / total_pessoas

print("A média aritmética das alturas é:", media_alturas)
