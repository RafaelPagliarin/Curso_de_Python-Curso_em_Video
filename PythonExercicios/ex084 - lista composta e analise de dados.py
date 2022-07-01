# faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# a) quantas pessoas foram cadastradas.
# b) uma lista com as pessoas mais pesadas.
# c) uma listagem com as pessoas mais leves.

pessoa = list()
lista = list()
maior = menor = 0
while True:
    cont = ' '
    pessoa.append(str(input('Nome: ')).strip())
    pessoa.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        elif pessoa[1] < menor:
            menor = pessoa[1]
    lista.append(pessoa[:])
    pessoa.clear()
    while cont not in 'SN':
        cont = str(input('Continuar? [S/N]')).strip().upper()
        if cont not in 'SN':
            print('resposta inválida.')
    if cont in 'N':
        break
print('-=' * 30)
print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'As pessoas com maior peso ({maior} kg): ', end='')
for i, v in enumerate(lista):
    if v[1] == maior:
        print(f' {v[0]}', end=' ')
print(f'\nAs pessoas com menor peso ({menor} kg): ', end='')
for i, v in enumerate(lista):
    if v[1] == menor:
        print(f' {v[0]}', end=' ')
print('\n-=' * 30)
