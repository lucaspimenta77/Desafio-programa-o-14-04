pontos_jogador_direita = 0
pontos_jogador_esquerda = 0

while True:
    ponto = input("Digite o código do ponto (D para jogador da direita, E para jogador da esquerda): ")

    if ponto == 'D':
        pontos_jogador_direita += 1
    elif ponto == 'E':
        pontos_jogador_esquerda += 1
    else:
        print("Entrada inválida! Digite apenas 'D' ou 'E' para registrar os pontos.")

    diferenca_pontos = abs(pontos_jogador_direita - pontos_jogador_esquerda)

    if pontos_jogador_direita >= 21 and diferenca_pontos >= 2:
        print("Jogador da direita venceu!")
        break
    elif pontos_jogador_esquerda >= 21 and diferenca_pontos >= 2:
        print("Jogador da esquerda venceu!")
        break
