# crie um programa que faça o computador jogar jokenpo com você.

# ===== imports ==========
from random import randint
from time import sleep

# ======== Prints e Menu =======
jpc = randint(1, 3)
print('-=-' * 7)
print('    Jogo: JokenPo')
print('-=-' * 7)
print('''    1 = pedra
    2 = papel
    3 = tesoura ''')
print('-=-' * 7)
jcpf = int(input('Qual sua jogada? '))
print()

# ======= Cores para Jogadas =======
if jpc == 1:
    rpc = '\33[34mpedra\33[m'
elif jpc == 2:
    rpc = '\33[35mpapel\33[m'
else:
    rpc = '\33[36mtesoura\33[m'

if jcpf == 1:
    rcpf = '\33[34mpedra\33[m'
elif jcpf == 2:
    rcpf = '\33[35mpapel\33[m'
else:
    rcpf = '\33[36mtesoura\33[m'

# ========= Descobrindo o Vencedor =========
if ((jpc == 1) and (jcpf == 3)) or ((jpc == 2) and (jcpf == 1)) or ((jpc == 3) and (jcpf == 2)):
    print('PROCESSANDO...')
    sleep(1)
    print(f'\33[31mVocê perdeu!\33[m PC escolheu {rpc} e você escolheu {rcpf}!')
elif jpc == jcpf:
    print('PROCESSANDO...')
    sleep(1)
    print(f'\33[33mEmpate!\33[m Ambos escolheram {rcpf}')
else:
    print('PROCESSANDO...')
    sleep(1)
    print(f'\33[32mVocê ganhou!\33[m PC escolheu {rpc} e você escolheu {rcpf}!')









