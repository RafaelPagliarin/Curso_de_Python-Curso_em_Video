# a confederação nacional de nataçào precisa de um programa que leia o ano de nascimentod e um atleta
# e mostre sua categoria, de acordo com a idade:
# até 9 anos: mirim
# até 14 anos: infantil
# até 19 anos: junior
# até 25 anos: senior
# acima: master

from datetime import date


nasci = int(input('Qual ano de nascimento do atleta? '))
idade = date.today().year - nasci

if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')

