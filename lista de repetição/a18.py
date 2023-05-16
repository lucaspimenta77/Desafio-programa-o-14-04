preco_ingresso = 5.00
decremento = 0.50
preco_minimo = 1.00

lucro_maximo = 0
preco_lucro_maximo = 0
ingressos_lucro_maximo = 0

print("Tabela de Preços e Lucros Esperados:")
print("Preço do Ingresso\tNúmero de Ingressos\tLucro Esperado")

while preco_ingresso >= preco_minimo:
    numero_ingressos = 120 + ((5.00 - preco_ingresso) / 0.50) * 26
    lucro = (preco_ingresso * numero_ingressos) - 200.00
    
    print(f"{preco_ingresso:.2f}\t\t\t{numero_ingressos:.0f}\t\t\t{lucro:.2f}")
    
    if lucro > lucro_maximo:
        lucro_maximo = lucro
        preco_lucro_maximo = preco_ingresso
        ingressos_lucro_maximo = numero_ingressos
    
    preco_ingresso -= decremento

print("\nLucro Máximo Esperado:")
print(f"Preço do Ingresso: R${preco_lucro_maximo:.2f}")
print(f"Número de Ingressos: {ingressos_lucro_maximo:.0f}")
print(f"Lucro Máximo: R${lucro_maximo:.2f}")
