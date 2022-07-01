#desenvolva um programa que leia 6 numeros inteiros e mostre a soma apenas daqueles que forem pares.
# se for impar, descondidere-o
s = 0
for c in range(0, 6):
    n = int(input(f'Digite o {c+1}º número: '))
    if n % 2 == 0:
        s += n
print()
print(f'A soma entre os números pares digitados é {s}.')
