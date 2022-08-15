# faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint

jogos = int(input('Quantos jogos você pretende fazer? '))
aux = list()
lista = list()
for contador in range(0, jogos):
    while len(aux) < 7:
        if len(aux) == 0:
            aux.append(randint(1, 60))
        else:
            r = randint(1, 60)
            if r not in aux:
                aux.append(r)
    aux.sort()
    lista.append(aux[:])
    aux.clear()
    print(lista[contador])

