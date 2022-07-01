# faça um programa que leia um número inteiro e diga se ele é ou não um número primo

n = int(input('Digite um número: '))
primo = True
for c in range(1, n + 1):
    if (n % c == 0) and (n != c) and (c != 1):
        primo = False

if primo:
    print(f'O número {n} é primo.')
elif not primo:
    print(f'O número {n} não é primo.')
