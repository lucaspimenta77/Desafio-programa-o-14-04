ultimo_cliente = 'ULTIMO'
total_geral = 0

while True:
    nome = input("Digite o nome do cliente: ")
    
    if nome == ultimo_cliente:
        break
    
    endereco = input("Digite o endereço do cliente: ")
    valor_compra = float(input("Digite o valor da compra: R$  "))
    
    if valor_compra > 500:
        desconto = 0.2
    else:
        desconto = 0.15
    
    valor_pagar = valor_compra - (valor_compra * desconto)
    total_geral += valor_pagar
    
    print("Total a pagar para", nome, "no endereço", endereco, ": R$", valor_pagar)
    print()
    
print("Total geral a pagar: R$", total_geral)
