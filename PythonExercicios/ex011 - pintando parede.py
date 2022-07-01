# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta
# necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2.00m²

larg = float(input('Qual a largura, em metros, da parede?'))
alt = float(input('Qual a altura, em metros, da parede?'))

print(f'A parede tem uma area de {larg*alt}m² e precisará de {(larg*alt)/2} litros de tinta para ser totalmente pintada.')