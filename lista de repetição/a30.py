# Leitura do preço do kWh por tipo de consumidor
preco_residencial = float(input("Digite o preço do kWh para consumidor residencial: "))
preco_comercial = float(input("Digite o preço do kWh para consumidor comercial: "))
preco_industrial = float(input("Digite o preço do kWh para consumidor industrial: "))

# Variáveis para armazenar a quantidade total de kWh consumidos
total_residencial = 0
total_comercial = 0
total_industrial = 0

# Variáveis para armazenar a quantidade total de consumidores de cada tipo
qtd_residencial = 0
qtd_comercial = 0
qtd_industrial = 0

# Variáveis para calcular a quantidade média geral de consumo
total_consumidores = 0
total_consumo = 0

# Leitura dos dados dos consumidores
n = int(input("Digite o número de consumidores: "))

for i in range(n):
    print(f"\nConsumidor {i + 1}:")
    identificacao = input("Número de identificação do consumidor: ")
    consumo = float(input("Quantidade de kWh consumidos durante o mês: "))
    tipo = input("Código do tipo de consumidor (R - residencial, C - comercial, I - industrial): ")

    # Cálculo do total a pagar por consumidor
    if tipo == 'R':
        total_pagar = consumo * preco_residencial
        total_residencial += consumo
        qtd_residencial += 1
    elif tipo == 'C':
        total_pagar = consumo * preco_comercial
        total_comercial += consumo
        qtd_comercial += 1
    elif tipo == 'I':
        total_pagar = consumo * preco_industrial
        total_industrial += consumo
        qtd_industrial += 1
    else:
        print("Código de tipo de consumidor inválido. Ignorando este consumidor.")
        continue

    # Impressão do número de identificação e total a pagar por consumidor
    print("Número de identificação:", identificacao)
    print("Total a pagar:", total_pagar)

    # Atualização das variáveis de quantidade média geral de consumo
    total_consumidores += 1
    total_consumo += consumo

# Impressão da quantidade total de kWh consumidos por tipo de consumidor
print("\nQuantidade total de kWh consumida:")
print("Residencial:", total_residencial)
print("Comercial:", total_comercial)
print("Industrial:", total_industrial)

# Cálculo e impressão da quantidade média geral de consumo
if total_consumidores > 0:
    media_consumo = total_consumo / total_consumidores
    print("\nQuantidade média geral de consumo:", media_consumo)
else:
    print("\nNenhum consumidor registrado.")

