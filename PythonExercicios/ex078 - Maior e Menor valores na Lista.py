# faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# no final, mostre qual foi o maiopr e o menor valor digitado e as suas respectivas posições na lista.

lista = list()
menor = maior = ''
for x in range(0, 5):
    lista.append(int(input(f'Digite o {x+1}º valor: ')))
    if x == 0:
        maior = menor = lista[x]
    else:
        if lista[x] > maior:
            maior = lista[x]
        if lista[x] < menor:
            menor = lista[x]

print(f'\nO maior valor foi {maior} nas posições: ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i+1}...', end=' ')
print(f'\nO menor valor foi {menor} nas posições: ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i+1}...', end=' ')