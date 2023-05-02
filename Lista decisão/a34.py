# Leitura das idades dos homens e mulheres
idade_homem1 = int(input("Digite a idade do primeiro homem: "))
idade_homem2 = int(input("Digite a idade do segundo homem: "))
idade_mulher1 = int(input("Digite a idade da primeira mulher: "))
idade_mulher2 = int(input("Digite a idade da segunda mulher: "))
if idade_homem1 == idade_homem2 or idade_mulher1 == idade_mulher2:
    print('Invalido! As idades entre iguais devem ser diferentes!')

# Cálculo da soma das idades do homem mais velho com a mulher mais nova
homem_mais_velho = max(idade_homem1, idade_homem2)
mulher_mais_nova = min(idade_mulher1, idade_mulher2)
soma_idades = homem_mais_velho + mulher_mais_nova
print("A soma das idades do homem mais velho com a mulher mais nova é:", soma_idades)

# Cálculo do produto da idade do homem mais novo com a mulher mais velha
homem_mais_novo = min(idade_homem1, idade_homem2)
mulher_mais_velha = max(idade_mulher1, idade_mulher2)
produto_idades = homem_mais_novo * mulher_mais_velha
print("O produto da idade do homem mais novo com a mulher mais velha é:", produto_idades)
