# faça um programa que calcule a soma de todos os números impares que são multiplos de 3 e que se encontram
# entre 1 e 500

x = 0
s = 0
for c in range(1, 501): # para economizar o uso da CPU, poderia colocar range(1, 501, 2) e ele calcularia pulando de 2 em 2
    if (c % 2 != 0) and (c % 3 == 0):
        s += c
        x += 1
print(f'O somátorio de todos os {x} valores solicitados é {s}')
