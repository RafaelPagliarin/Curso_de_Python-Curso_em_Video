# faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# se ele ainda vai se alistar ao serviço militar
# se é a hora de se alistar
# se já passou do tempo de alistamento.

# seu programa também deverá mostrar o tempo que falta ou passou do prazo.

from datetime import date
ano = int(input('Qual seu ano de nascimento?'))

idade = date.today().year - ano

if idade < 18:
    print(f'Você ainda vai se alistar para o serviço militar. Faltam {18-idade} anos')
if idade == 18:
    print('Está na hora de se alistar! Procure o posto de alistamento mais próximo de sua residência.')
if idade > 18:
    print(f'Se você não se alistou ainda, já passou da hora. Você está {idade-18} anos atrasado.')