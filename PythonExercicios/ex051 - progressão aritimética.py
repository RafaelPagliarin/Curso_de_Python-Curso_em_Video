# desenvolva um programa que leia o primeiro termo e a razão de uma PA. no final, mostre os 10 primeiros termos
# dessa PA.

i = int(input('Qual o 1º termo da P.A. ? '))
r = int(input('Qual a razão da P.A. ? '))

for c in range(i, (i+10*r), r):
    print(c, end=' ')
print('Fim.')

