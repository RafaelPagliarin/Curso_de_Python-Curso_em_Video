#desenvolva um programa que leia 6 numeros inteiros e mostre a soma apenas daqueles que forem pares.
# se for impar, descondidere-o

soma_par = 0
for c in range(1, 7):
    numero = int(input(f'Digite o {c}º número: '))
    if numero % 2 == 0:
        soma_par += numero

print()
print(f'A soma entre os números pares digitados é {soma_par}.')
