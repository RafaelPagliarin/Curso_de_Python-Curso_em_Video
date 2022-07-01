# crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
# o valor 999. que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
# descondiserando o flag

n = ''
x = 0
c = 0
while n != 999:
    n = int(input('Digite um número (999 para parar) : '))
    x += n
    c += 1
print()
print(f'Foram digitados {c} números, e a soma entre eles é {x}')
