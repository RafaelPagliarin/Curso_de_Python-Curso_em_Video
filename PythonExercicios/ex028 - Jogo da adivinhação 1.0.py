#Escreva um programa que faça o pc "pensar" em um número inteiro entre 0 e 5
#e peça para o usuário tentar descobrir qual foi o número escolhido pelo py_compile
#o programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint
from time import sleep
sorteado = randint(0, 5)

print('-=-' * 20)
print('| Vou pensar em um número entre 0 e 5. Tente adivinhar...  |')
print('-=-' * 20)
tentativa = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(2)
if sorteado == tentativa:
    input(f'Parabéns, você acertou! valor sorteado: {sorteado}.')
else:
    input(f'Você errou! Pensei em {sorteado} e não em {tentativa}.')
