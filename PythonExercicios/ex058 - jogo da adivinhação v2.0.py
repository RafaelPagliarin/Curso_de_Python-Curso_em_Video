# melhore o jogo do desafio 28 onde o pc vai "pensar" em um número entre 0 e 10. só que agora o jogador vai tentar
# adivinhar até acertar, mostrando no final quantos palpites foram necessários para acertar.

from random import randint

palpite_jogador = ''
c = 0
valor_sorteado = randint(0, 10)

print('-='*13)
print('Jogo da Adivinhação v2.0:')
print('-='*13)
print()

while palpite_jogador != valor_sorteado:
    palpite_jogador = int(input('Tente adivinhar qual número entre 0 e 10 o computador pensou: '))
    if palpite_jogador not in range(0, 11):
        print(f'Valor {palpite_jogador} é invalido. Tente novamente')
        continue
    c += 1
    if palpite_jogador != valor_sorteado:
        if palpite_jogador > valor_sorteado:
            print('Errou para mais, tente novamente...')
        elif palpite_jogador < valor_sorteado:
            print('Errou para menos, tente novamente...')

print()
print(f'Correto! Você acertou após {c} tentativas!')