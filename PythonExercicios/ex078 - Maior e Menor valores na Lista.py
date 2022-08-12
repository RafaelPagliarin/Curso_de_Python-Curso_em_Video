# faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# no final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = list()
for x in range(5):
    lista.append(int(input(f'Digite o {x+1}º valor: ')))

for indice, valor in enumerate(lista):
    if indice == 0:
        maior = menor = valor
        indice_maior = indice_menor = indice
    else:
        if valor > maior:
            maior = valor
            indice_maior = indice
        if valor < menor:
            menor = valor
            indice_menor = indice

print(f'O maior valor foi {maior} na posição {indice_maior + 1}')
print(f'O menor valor foi {menor} na posição {indice_menor + 1}')

