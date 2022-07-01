# crie um programa que leia vários números inteiros pelo teclado. o programa só vai parar quando o usuário digitar o
# valor 999. no final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

s = x = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    s += n
    x += 1

print(f'foram digitados {x} números e a soma entre eles é {s}')
