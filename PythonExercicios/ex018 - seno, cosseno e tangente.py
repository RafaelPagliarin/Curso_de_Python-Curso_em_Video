# faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo

from math import sin, cos, tan, radians

print(f'Calculadora de Seno, Cosseno e Tangente: ')
rad = float(input('Digite um ângulo: '))
print(f' seno de {rad}º = {sin(radians(rad)):.2f} \n'
      f' cosseno de {rad}º = {cos(radians(rad)):.2f} \n'
      f' tangente de {rad}º = {tan(radians(rad)):.2f}')

