# crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numeros_tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for n in numeros_tupla:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros_tupla)}.')
print(f'O menor valor sorteado foi {min(numeros_tupla)}.')

