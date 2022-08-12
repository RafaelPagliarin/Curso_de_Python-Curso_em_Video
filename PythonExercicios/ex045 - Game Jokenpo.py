# crie um programa que faça o computador jogar jokenpo com você.

# ===== imports ==========
from random import randint
from time import sleep

# ======== Prints e Menu =======
valor_pc = randint(1, 3)
print('-=-' * 7)
print('    Jogo: JokenPo')
print('-=-' * 7)
print('''    1 = pedra
    2 = papel
    3 = tesoura ''')
print('-=-' * 7)
valor_usuario = int(input('Qual sua jogada? '))
print()

# ======= Cores para Jogadas =======
if valor_pc == 1:
    jogada_pc = '\33[34mpedra\33[m'
elif valor_pc == 2:
    jogada_pc = '\33[35mpapel\33[m'
else:
    jogada_pc = '\33[36mtesoura\33[m'

if valor_usuario == 1:
    jogada_usuario = '\33[34mpedra\33[m'
elif valor_usuario == 2:
    jogada_usuario = '\33[35mpapel\33[m'
else:
    jogada_usuario = '\33[36mtesoura\33[m'

# ========= Descobrindo o Vencedor =========
if ((valor_pc == 1) and (valor_usuario == 3)) or\
   ((valor_pc == 2) and (valor_usuario == 1)) or\
   ((valor_pc == 3) and (valor_usuario == 2)):
    print('PROCESSANDO...')
    sleep(1)
    print(f'\33[31mVocê perdeu!\33[m PC escolheu {jogada_pc} e você escolheu {jogada_usuario}!')
elif valor_pc == valor_usuario:
    print('PROCESSANDO...')
    sleep(1)
    print(f'\33[33mEmpate!\33[m Ambos escolheram {jogada_usuario}')
else:
    print('PROCESSANDO...')
    sleep(1)
    print(f'\33[32mVocê ganhou!\33[m PC escolheu {jogada_pc} e você escolheu {jogada_usuario}!')









