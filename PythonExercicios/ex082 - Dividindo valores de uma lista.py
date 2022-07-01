# crie um programa que vai ler vários números e colocar em uma lista.
# depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente.
# ao final, mostre o conteúdo das 3 listas geradas.


lista = []
pares = []
impares = []

while True:
    cont = ' '
    lista.append(int(input('Digite um número: ')))
    while cont not in 'SN':
        cont = str(input('Continuar [S/N] ? ')).strip().upper()[0]
        if cont not in 'SN':
            print('Opção Inválida.')
    if cont in 'N':
        break

for n, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print('=-=' * 15)
print(f'Lista = {lista}')
print(f'Pares = {pares}')
print(f'Impares = {impares}')
print('=-=' * 15)
