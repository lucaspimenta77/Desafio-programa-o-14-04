quantidade_tinta = float(input("Digite a quantidade de tinta na caneta: "))

while quantidade_tinta > 0:
    print("Enquanto tem tinta a caneta escreve...")
    quantidade_tinta -= quantidade_tinta * 0.02

    if quantidade_tinta < 0.01:  # Considerando uma margem de erro de 0.01
        quantidade_tinta = 0

print("A caneta parou de escrever por falta de tinta.")
