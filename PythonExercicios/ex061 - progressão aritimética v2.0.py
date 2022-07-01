# refaça o desafio 51, lendo o primeiro termo de uma PA e a razão, mostrando os 10 primeiros termos da progressão
# usando a estrutura while


i = int(input('Qual o 1º termo da P.A. ? '))
r = int(input('Qual a razão da P.A. ? '))
t = int(input('Quantos termos você quer ver?'))
x = 0

while x < t:
    if x == (t-1):
        print(i + r * x)
    else:
        print(i+r*x, end=' ➡ ')
    x += 1
