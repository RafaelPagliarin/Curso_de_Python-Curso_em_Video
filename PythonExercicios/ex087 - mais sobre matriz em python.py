# aprimore o desafio anterior, mostrando no final
# a soma de todos os valores pares
# a soma dos valores da terceira coluna
# o maior valor da segunda linha

matriz = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
pares = s = m = 0
print()
for i in range(0, 3):
    for x in range(0, 3):
        print(f'[{(matriz[i][x])}] ', end='')
    print()
print()
for i in range(0, 3):
    for x in range(0, 3):
        matriz[i][x] = int(input(f'Digite o valor de {matriz[i][x]} :'))
print()
for i in range(0, 3):
    s += matriz[i][2]
    for x in range(0, 3):
        if x == 0:
            m = matriz[1][0]
        else:
            if matriz[1][x] > m:
                m = matriz[1][x]
        print(f'[{(matriz[i][x]):0>2}] ', end='')
        if matriz[i][x] % 2 == 0:
            pares += matriz[i][x]
    print()
print(f'A soma de todos os valores pares é: {pares}.')
print(f'A soma de todos os valores da terceira coluna é: {s}.')
print(f'O maior valor da segunda linha é: {m}.')
