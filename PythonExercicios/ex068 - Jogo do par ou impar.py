# faça um programa que jogue par ou impar com o computador.
# o jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou
# no final do jogo.

from random import randint
vit = 0
print('-=' * 10)
print('Jogo do Par ou Ímpar')
print('-=' * 10)
while True:
    player = -1
    pori = ' '
    pc = randint(0, 5)
    while pori not in 'PI':
        pori = str(input('Você quer Par ou Impar? ')).strip().upper()[0]
        if pori not in 'PI':
            print('Opção inválida.')
    while player < 0 or player > 5:
        player = int(input('Sua jogada [0 a 5]:'))
        if player < 0 or player > 5:
            print('Jogada inválida.')
    if (player + pc) % 2 == 0:
        resultado = 'Par'
        res = 'P'
    else:
        resultado = 'Ímpar'
        res = 'I'
    if pori != res:
        break
    else:
        vit += 1
        print(f'\33[32mVocê ganhou!\33[m Você jogou {player} e o PC jogou {pc}, dando um resultado {resultado}.')
        print()
print()
print(f'\33[31mVocê perdeu\33[m após {vit} vitórias consecutivas sobre o PC!')