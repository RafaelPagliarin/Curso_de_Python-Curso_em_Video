# crie um programa que leia o ano de nascimento de 7 pessoas
# no final mostre quantas pessoas atingiram a maioridade e quantas não (maioridade com 21 anos)

from datetime import date

menores = 0
maiores = 0

for c in range(0, 7):
    ano_nascimento = int(input(f'Digite o ano de nascimento da {c + 1}º pessoa :'))
    idade = date.today().year - ano_nascimento
    if idade < 21:
        menores += 1
    else:
        maiores += 1

print(f'{menores} pessoas são menores de 21 anos nesse grupo.')
print(f'{maiores} pessoas são maiores de 21 anos nesse grupo')

