# faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint

j = int(input('Quantos jogos você pretende fazer? '))
aux = list()
lista = list()
for c in range(0, j):
    while True:
        if len(aux) == 0:
            aux.append(randint(1, 60))
        else:
            r = randint(1, 60)
            if r not in aux:
                aux.append(r)
        if len(aux) == 6:
            break
    aux.sort()
    lista.append(aux[:])
    aux.clear()

    print(lista[c])

