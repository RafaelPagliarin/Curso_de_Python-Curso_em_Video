# escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos
# de uma sequencia de fibonacci

elementos = int(input('Quantos elementos da sequência de Fibonacci você deseja ver? '))
contador = 0  #contador de elementos
x = 0  #valor do primeiro termo e depois de t(n-2)
y = 1  #valor do segundo termo e depois de t(n-1)
z = '' #valor do termo atual para tn > 2
while contador < elementos:
    if contador == 0:
        print(x, end='➡')
    elif contador == 1:
        print(y, end='➡')
    else:
        z = x + y
        if contador == (elementos - 1):
            print(f'{z}')
        else:
            print(f'{z}', end='➡')
        x = y
        y = z
    contador += 1

    