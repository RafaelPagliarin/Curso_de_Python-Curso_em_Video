# crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
# o valor 999. que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
# descondiserando o flag

valor = ''
somatorio = 0
c = 0
while valor != 999:
    valor = int(input('Digite um número (999 para parar) : '))
    somatorio += valor
    c += 1
print()
print(f'Foram digitados {c} números, e a soma entre eles é {somatorio}')
