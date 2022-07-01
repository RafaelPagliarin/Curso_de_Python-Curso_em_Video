# crie um programa que faça o computador jogar jokenpo com você.

# ===== imports ==========
from random import randint
from time import sleep

# ==============
itens = ('\33[34mPedra\33[m', '\33[35mPapel\33[m', '\33[36mTesoura\33[m')
pc = randint(0, 2)

# ======== Prints e Menu =======
print('-=' * 11)
print('    Jogo: JokenPo')
print('-=' * 11)
print('''    0 = \33[34mPedra\33[m
    1 = \33[35mPapel\33[m
    2 = \33[36mTesoura\33[m ''')
print('-=' * 11)
cpf = int(input('Qual sua jogada? '))
print()

# ========= Descobrindo o Vencedor =========
if ((pc == 0) and (cpf == 2)) or ((pc == 1) and (cpf == 0)) or ((pc == 2) and (cpf == 1)):
    print('PROCESSANDO...')
    sleep(1)
    print(f'\33[31mVocê perdeu!\33[m PC escolheu {itens[pc]} e você escolheu {itens[cpf]}!')
elif pc == cpf:
    print('PROCESSANDO...')
    sleep(1)
    print(f'\33[33mEmpate!\33[m Ambos escolheram {itens[cpf]}')
else:
    print('PROCESSANDO...')
    sleep(1)
    print(f'\33[32mVocê ganhou!\33[m PC escolheu {itens[pc]} e você escolheu {itens[cpf]}!')