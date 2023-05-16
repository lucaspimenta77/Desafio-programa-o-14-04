contas_encerradas = 0

while True:
    print("----- Menu Principal -----")
    print("1. Encerrar conta de um hóspede")
    print("2. Verificar número de contas encerradas")
    print("3. Finalizar a execução")

    opcao = input("Escolha uma opção (1, 2 ou 3): ")

    if opcao == '1':
        nome = input("Digite o nome do hóspede: ")
        num_diarias = int(input("Digite o número de diárias: "))

        if num_diarias < 15:
            taxa_servicos = 7.50
        elif num_diarias == 15:
            taxa_servicos = 6.50
        else:
            taxa_servicos = 5.00

        total_pagar = 50.00 * num_diarias + taxa_servicos
        print("Nome do hóspede:", nome)
        print("Total a ser pago:", total_pagar)
        contas_encerradas += 1

    elif opcao == '2':
        print("Número de contas encerradas:", contas_encerradas)

    elif opcao == '3':
        print("Finalizando a execução...")
        break

    else:
        print("Opção inválida. Escolha uma opção válida (1, 2 ou 3).")
