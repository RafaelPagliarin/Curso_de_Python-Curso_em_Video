# crie um programa que crie uma matriz 3x3 e preencha com valores lidos pelo teclado.
# no final, mostre a matriz na tela, com a formatação correta.

matriz = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
menu = '  Matriz 3x3:  '
print('=' * len(menu))
print(f'{menu}')
print('=' * len(menu))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{(matriz[linha][coluna])}] ', end='')
    print()
print('=' * len(menu))
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = input(f'Digite o valor de {matriz[linha][coluna]} :')
print('=' * len(menu))
print('Matriz 3x3:')
print('=' * len(menu))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{(matriz[linha][coluna]):0>3}] ', end='')
    print()
print('=-=' * 7)


'''
matriz = [ [], [], [] ]
matriz[0] = A,B,C 
matriz[1] = D,E,F 
matriz[2] = G,H,I

A = 0,0
B = 0,1
C = 0,2
D = 1,0
E = 1,1
F = 1,2
G = 2,0
H = 2,1
I = 2,2
'''