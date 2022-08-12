# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
# considere US$ 1.00 = R$ 3.27

din = float(input('Quantos reais você tem na carteira? \33[32mR$\33[m'))
print()
print(f'Com \33[33mR${din:.2f}\33[m você pode comprar \33[31mUS${din/3.27:.2f}\33[m')
