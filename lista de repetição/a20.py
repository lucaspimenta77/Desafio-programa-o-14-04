total_biscoitos_quebrados = 0

for dia in range(1, 6):
    biscoitos_quebrados = 1  

    for hora in range(1, 17):
        total_biscoitos_quebrados += biscoitos_quebrados
        biscoitos_quebrados *= 3

    print(f"No final do dia {dia}, a quantidade de biscoitos quebrados é: {total_biscoitos_quebrados}")
    total_biscoitos_quebrados = 0 
