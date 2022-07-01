# crie um programa que leia o ano de nascimento de 7 pessoas
# no final mostre quantas pessoas atingiram a maioirdade e quantas não (maioridade com 21 anos)

from datetime import date
n = 0
m = 0
for c in range(0, 7):
    nasc = int(input(f'Digite o ano de nascimento da {c+1}º pessoa :'))
    if (date.today().year - nasc) < 21:
        n += 1
    else:
        m += 1
print(f'{n} pessoas são menores de 21 anos nesse grupo.')
print(f'{m} pessoas são maiores de 21 anos nesse grupo')