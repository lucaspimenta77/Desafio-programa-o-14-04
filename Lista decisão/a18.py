# Faça um algoritmo que verifique se uma letra digitada é vogal ou consoante.

letra = str(input("Digite uma letra: "))
if letra in "AEIOUaeiou":
    print("Vogal")
else:
    print("Consoante")
