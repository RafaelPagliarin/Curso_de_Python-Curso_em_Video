# desenvolva um programa que pergunte a distância de uma viagem em km.
# calcule o preço da passagem, cobrando R$0.50 por km para viagens de até 200km e R$0.45 para viagens maiores

dist = float(input('Qual a distância da viagem, em km? '))
if dist <= 200.0:
    print(f'O preço da passagem é R${dist*0.5:.2f}')
else:
    print(f'O preço da passagem é R${dist*0.45:.2f}')

