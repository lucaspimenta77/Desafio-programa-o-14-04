#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). 

arquivo = float(input("Digite o tamanho do arquivo em MB: "))
internet = float(input("Digite a velocidade do link de Internet em Mbps: "))
download = (arquivo * 8) / (internet / 60)
print(f"O tempo de download do arquivo é de aproximadamente {download} minutos.")