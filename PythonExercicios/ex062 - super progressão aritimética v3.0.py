# melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# o programa encerra quando ele disser que quer mostrar 0 termos.

i = int(input('Qual o 1º termo da P.A. ? '))
r = int(input('Qual a razão da P.A. ? '))
t = int(input('Quantos termos você quer ver?'))
print()
c = 0
x = 0
t2 = ''
while t2 != 0:
    while x < t:
        if x == (t-1):
            print(i+r*x)
        else:
            print(i+r*x, end=' ➡ ')
        x += 1
    print()
    t2 = int(input('Quantos termos vc quer mostrar a mais?'))
    t += t2
print('Fim')
