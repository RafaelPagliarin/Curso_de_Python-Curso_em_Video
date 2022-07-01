# faça um programa que leia um número qualquer e mostre seu fatorial
print('-=' * 12)
print('Calculadora de Fatorial')
print('-=' * 12)
n = int(input('Digite um número: '))
c = 1
r = 1
while n >= c:
    r *= c
    if c == 1:
        print(f'{n}! = {c}', end=' x ')
    elif c == n:
        print(f'{c} = {r}')
    else:
        print(f'{c}', end=' x ')
    c += 1

# ======== usando o "factorial" =============
# f = factorial(n)
# print(f'O fatorial de {n}! é {f}')

# ======== para mostrar todos os números ============
