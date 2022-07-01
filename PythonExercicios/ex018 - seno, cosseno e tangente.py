# faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo

from math import sin, cos, tan, radians

rad = float(input('Digite um ângulo: '))
print(f' seno de {rad} = {sin(radians(rad)):.2f} \n cosseno de {rad} = {cos(radians(rad)):.2f} \n tangente de {rad} = {tan(radians(rad)):.2f}')
