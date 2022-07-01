# faça um programa que tenha uma função chamada contador(), que receba 3 parametros: inicio, fim e passo e realize a contagem
# seu programa tem que realizar 3 contagens através da função criada:
# a. de 1 até 10, de 1 em 1
# b. de 10 até 0, de 2 em 2
# uma contagem personalizada
from time import sleep


def contador(i, f, r):
    print('~' * 40)
    print(f'Contagem de {i} até {f} com passo {r}...')
    sleep(2)
    if r == 0:
        r = 1
    if r < 0:
        r *= -1
    if i < f:
        for c in range(i, f + 1, r):
            print(c, end=' ')
            sleep(0.5)
        print(' Fim...')
    else:
        r *= -1
        for c in range(i, f - 1, r):
            print(c, end=' ')
            sleep(0.5)
        print(' Fim...')


# Programa

contador(1, 10, 1)
print()
contador(10, 0, 2)
print()
print('~' * 40)
print('Contagem Personalizada:')
inicio = int(input('Inicio da contagem: '))
final = int(input('Final da contagem: '))
passo = int(input('Passo da contagem: '))
contador(inicio, final, passo)
