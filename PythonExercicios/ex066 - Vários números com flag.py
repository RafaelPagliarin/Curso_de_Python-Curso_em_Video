# crie um programa que leia vários números inteiros pelo teclado. o programa só vai parar quando o usuário digitar o
# valor 999. no final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

somatorio = contador = 0
while True:
    valor = int(input('Digite um valor (999 para parar): '))
    if valor == 999:
        break
    somatorio += valor
    contador += 1

print(f'foram digitados {contador} números e a soma entre eles é {somatorio}')
