# crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua posição inteira
# ex: digite um número: 6.127
# o número 6.127 tem a parte inteira 6.

from math import trunc
n = float(input('Digite um número: '))
print(f'o número {n} tem a parte inteira {trunc(n)}')

# print(f'O número {n} tem a parte inteira {int(n)}') --- mostra a parte inteira do número, também funciona