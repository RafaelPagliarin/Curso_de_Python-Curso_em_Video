# crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada uma em um dicionário,
# e todos os dicionários em uma lista. No final, mostre:
# 1. quantas pessoas foramm cadastradas
# 2. A média de idade do grupo.
# 3. umma lista com todas as mulheres.
# 4. uma lista com todas as pessoas comm idade acima da média

from datetime import date
lista = list()
media = tot = 0
pessoas = dict()
while True:
    cont = sexo = ' '
    pessoas.clear()
    pessoas['nome'] = str(input('Digite o nome: ')).strip()
    while sexo not in 'FM':
        sexo = str(input('Digite o sexo [F/M]: ')).strip().upper()[0]
        if sexo not in 'FM':
            print('Erro! Por favor, digite apenas M ou F.')
    pessoas['sexo'] = sexo
    nasc = int(input('Ano de nascimento: '))
    pessoas['idade'] = date.today().year - nasc
    tot += (date.today().year - nasc)
    lista.append(pessoas.copy())

    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
        if cont not in 'SN':
            print('Erro! Por favor, digite apenas S ou N.')
    if cont in 'N':
        print('\nencerrando cadastros..')
        break
print('-=' * 20)
print(f'A) Foram cadastradas {len(lista)} pessoas.')
media = tot/len(lista)
print(f'B) A média de idade do grupo é: {media:5.2f} anos.')
print(f'C) As mulheres do grupo são: ', end='')
for p in lista:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print(f'\nD) As pessoas acima da média de idade do grupo são: ')
for p in lista:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('-=' * 20)
