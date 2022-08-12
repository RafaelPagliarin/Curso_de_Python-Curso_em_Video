# faça um programa que jogue par ou impar com o computador.
# o jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou
# no final do jogo.

from random import randint


vitorias = 0
print('-=' * 10)
print('Jogo do Par ou Ímpar')
print('-=' * 10)
while True:
    usuario = -1
    par_ou_impar = ' '
    pc = randint(0, 5)
    while par_ou_impar not in 'PI':
        par_ou_impar = str(input('Você quer Par ou Impar? ')).strip().upper()[0]
        if par_ou_impar not in 'PI':
            print('Opção inválida.')
    while usuario < 0 or usuario > 5:
        usuario = int(input('Sua jogada [0 a 5]:'))
        if usuario < 0 or usuario > 5:
            print('Jogada inválida.')
    if (usuario + pc) % 2 == 0:
        resultado = 'Par'
    else:
        resultado = 'Impar'
    if par_ou_impar != resultado[0]:
        break
    else:
        vitorias += 1
        print(f'\33[32mVocê ganhou!\33[m Você jogou {usuario} e o PC jogou {pc}, dando um resultado {resultado}.')
        print()
print()
print(f'Você jogou {usuario} e o PC jogou {pc}, dando um resultado {resultado}')
print(f'\33[31mVocê perdeu\33[m após {vitorias} vitórias consecutivas sobre o PC!')