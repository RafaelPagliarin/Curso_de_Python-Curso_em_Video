# faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo,
# calcule e mostre o comprimento da hipotenusa.

'''
outra resolução seria:

from math import sqrt
co = float(input('Digite o valor do cateto oposto '))
ca = float(input('Digite o valor do cateto adjacente '))

print(f'O valor da hipotenusa para cateto oposto {co} e cateto adjacente {ca} é {sqrt(ca**2 + co**2):.2f}')
'''


from math import hypot
co = float(input('Digite o valor do Cateto Oposto '))
ca = float(input('Digite o valor do Cateto Adjacente '))
print(f'A hipotenusa vai medir {hypot(co, ca):.2f}')