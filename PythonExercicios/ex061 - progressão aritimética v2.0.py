# refaça o desafio 51, lendo o primeiro termo de uma PA e a razão, mostrando os 10 primeiros termos da progressão
# usando a estrutura while


inicio = int(input('Qual o 1º termo da P.A. ? '))
razão = int(input('Qual a razão da P.A. ? '))
termos = int(input('Quantos termos você quer ver?'))
x = 0

while x < termos:
    if x == (termos - 1):
        print(inicio + razão * x)
    else:
        print(inicio + razão * x, end=' ➡ ')
    x += 1
