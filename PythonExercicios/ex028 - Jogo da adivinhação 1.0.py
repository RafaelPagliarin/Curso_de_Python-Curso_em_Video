#Escreva um programa que faça o pc "pensa" em um número inteiro entre 0 e 5
#e peça para o usuário tentar descobrir qual foi o número escolhido pelo py_compile
#o programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint
from time import sleep
rand = randint(0,5)
print()
print('-=-' * 20)
print('| Vou pensar em um número entre 0 e 5. Tente adivinhar...  |')
print('-=-' * 20)
tent = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(2)
if rand == tent:
    input(f'Parabéns, você acertou! valor sorteado: {rand}.')
else:
    input(f'Você errou! Pensei em {rand} e não em {tent}.')
