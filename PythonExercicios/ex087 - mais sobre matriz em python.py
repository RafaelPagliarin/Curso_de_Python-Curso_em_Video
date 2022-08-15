# aprimore o desafio anterior, mostrando no final
# a soma de todos os valores pares
# a soma dos valores da terceira coluna
# o maior valor da segunda linha

matriz = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
pares = soma = maior_segunda_linha = 0
print()
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{(matriz[linha][coluna])}] ', end='')
    print()
print()
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o valor de {matriz[linha][coluna]} :'))
print()
for linha in range(0, 3):
    soma += matriz[linha][2]
    for coluna in range(0, 3):
        if coluna == 0:
            maior_segunda_linha = matriz[1][0]
        else:
            if matriz[1][coluna] > maior_segunda_linha:
                maior_segunda_linha = matriz[1][coluna]
        print(f'[{(matriz[linha][coluna]):0>2}] ', end='')
        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna]
    print()
print(f'A soma de todos os valores pares é: {pares}.')
print(f'A soma de todos os valores da terceira coluna é: {soma}.')
print(f'O maior valor da segunda linha é: {maior_segunda_linha}.')
