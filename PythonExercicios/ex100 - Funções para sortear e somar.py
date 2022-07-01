# faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e SomaPar(). A primeira função
# vai sortear 5 números e vai colocalos dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES
# sorteados pela função anterior

from random import randint
from time import sleep


def sorteio():
    print('Sorteando 5 valores: ', end=' ')
    sleep(0.5)
    for i in range(0, 5):
        n = randint(0, 99)
        numeros.append(n)
        print(n, end=' ')
        sleep(0.5)
    print('... pronto!')
    sleep(1)


def somapar():
    s = 0
    for k, v in enumerate(numeros):
        if v % 2 == 0:
            s += v
    print(f'A soma de todos os valores pares é : {s}')


# Programa Principal
numeros = list()
sorteio()
somapar()
