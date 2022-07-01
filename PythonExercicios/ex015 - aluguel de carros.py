# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

qm = float(input('Quantos quilometros foram rodados com o veículo?'))
tem = float(input('Quantos dias o veículo permaneceu alugado?'))

print(f'O total a pagar pela locação do carro é de R${(60*tem)+(0.15*qm)}')
