# melhore o jogo do desafio 28 onde o pc vai "pensar" em um número entre 0 e 10. só que agora o jogador vai tentar
# adivinhar até acertar, mostrando no final quantos palpites foram necessários para acertar.

from random import randint

r = ''
c = 0
n = randint(0, 10)

print('-='*13)
print('Jogo da Adivinhação v2.0:')
print('-='*13)
print()

while r != n:
    r = int(input('Tente adivinhar qual número entre 0 e 10 o computador pensou: '))
    if r != '':
        c += 1
    if r != n:
        if r > n:
            print('Errou para mais, tente novamente...')
        elif r < n:
            print('Errou para menos, tente novamente...')

print()
print(f'Correto! Você acertou após {c} tentativas!')