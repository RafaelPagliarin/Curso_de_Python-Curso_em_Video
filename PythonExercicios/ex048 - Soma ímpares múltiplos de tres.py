# faça um programa que calcule a soma de todos os números impares que são multiplos de 3 e que se encontram
# entre 1 e 500

contador_impares = 0
soma_impares = 0
for numero in range(1, 501): # para economizar o uso da CPU, poderia colocar range(1, 501, 2) e ele calcularia pulando de 2 em 2
    if (numero % 2 != 0) and (numero % 3 == 0):
        soma_impares += numero
        contador_impares += 1
print(f'O somátorio de todos os {contador_impares} valores solicitados é {soma_impares}')
