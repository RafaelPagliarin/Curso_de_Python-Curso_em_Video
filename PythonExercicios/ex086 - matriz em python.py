# crie um programa que crie uma matriz 3x3 e preencha com valores lidos pelo teclado.
# no final, mostre a matriz na tela, com a formatação correta.

matriz = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
print('=-=' * 7)
print(f'Matriz 3x3:')
print('=-=' * 7)
for i in range(0, 3):
    for x in range(0, 3):
        print(f'[{(matriz[i][x])}] ', end='')
    print()
print('=-=' * 7)
for i in range(0, 3):
    for x in range(0, 3):
        matriz[i][x] = input(f'Digite o valor de {matriz[i][x]} :')
print('=-=' * 7)
print('Matriz 3x3:')
print('=-=' * 7)
for i in range(0, 3):
    for x in range(0, 3):
        print(f'[{(matriz[i][x]):0>3}] ', end='')
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