 # melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# o programa encerra quando ele disser que quer mostrar 0 termos.

inicio = int(input('Qual o 1º termo da P.A. ? '))
razão = int(input('Qual a razão da P.A. ? '))
termos = int(input('Quantos termos você quer ver?'))
print()
x = 0
mais_termos = ''
while mais_termos != 0:
    while x < termos:
        if x == (termos - 1):
            print(inicio + razão * x)
        else:
            print(inicio + razão * x, end=' ➡ ')
        x += 1
    print()
    mais_termos = int(input('Quantos termos vc quer mostrar a mais?'))
    termos += mais_termos
print('Fim')
