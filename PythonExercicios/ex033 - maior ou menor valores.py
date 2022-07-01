# faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))

if a > b and a > c:
    maior = a
    if b > c:
        menor = c
    else:
        menor = b
else:
    if b > c:
        maior = b
        if a > c:
            menor = c
        else:
            menor = a
    else:
        maior = c
        if a > b:
            menor = b
        else:
            menor = a

print(f'O maior número digitado é {maior} e o menor é {menor}.')


