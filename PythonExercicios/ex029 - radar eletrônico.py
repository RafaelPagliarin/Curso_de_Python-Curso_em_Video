#escreva um programa que leia a velocidade de um carro
#se ele ultrapassar 80km/h , mostre uma mensagem dizendo que ele foi multado
#a multa vai custar R$7.00 por cada km/h acima do limite

vel = float(input('Digite a velocidade atual do veículo, em km/h: '))
if vel > 80.0:
    print(f'Você estava acima da velocidade máxima permitida, você foi multado e o valor da multa é de R${(vel-80)*7:.2f}')
else:
    print('Você estava dentro do limite de velocidade.')

