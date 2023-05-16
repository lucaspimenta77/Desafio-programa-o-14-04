limite_diario = float(input("Digite o limite diário de pesca (em quilogramas): "))
peso_total = 0.0

while True:
    peso_peixe = float(input("Digite o peso do peixe (em gramas): "))
    peso_total += peso_peixe / 1000  # Convertendo de gramas para quilogramas

    if peso_total > limite_diario:
        print("Limite diário de pesca excedido!")
        break

    opcao = input("Deseja informar o peso de mais um peixe? (s/n): ")

    while opcao.lower() != 's' and opcao.lower() != 'n':
        print("Opção inválida. Digite 's' para sim ou 'n' para não.")
        opcao = input("Deseja informar o peso de mais um peixe? (s/n): ")

    if opcao.lower() == 'n':
        break

print("Peso total da pesca:", peso_total, "quilogramas")
