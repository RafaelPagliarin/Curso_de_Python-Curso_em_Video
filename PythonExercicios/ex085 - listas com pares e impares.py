# crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e impares. No final, mostre os valores pares e impares em ordem crescente

lista = [[], []]
for i in range(0, 7):
    valor = int(input(f'Digite o {i+1}º valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print('=-=' * 15)
print(f'Pares: {lista[0]}')
print(f'Impares: {lista[1]}')
print('=-=' * 15)