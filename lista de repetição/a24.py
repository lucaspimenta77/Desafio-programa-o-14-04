soma_idades = 0
qtd_pessoas = 0

while True:
    idade = int(input("Digite a idade da pessoa: "))

    if idade > 0:
        soma_idades += idade
        qtd_pessoas += 1

    opcao = input("Deseja digitar mais um valor? (s/n): ")

    while opcao.lower() != 's' and opcao.lower() != 'n':
        print("Opção inválida. Digite 's' para sim ou 'n' para não.")
        opcao = input("Deseja digitar mais um valor? (s/n): ")

    if opcao.lower() == 'n':
        break

if qtd_pessoas > 0:
    media_idades = soma_idades / qtd_pessoas
    print("A idade média do grupo de pessoas é:", media_idades)
else:
    print("Nenhum valor válido foi digitado.")
