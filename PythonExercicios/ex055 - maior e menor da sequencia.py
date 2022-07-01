# faça um programa que leia o peso de 5 pessoas e mostre o maior e menor peso lidos.


for c in range(0, 5):
    peso = float(input(f'Digite o peso da {c+1}º pessoa, em kg: '))
    if c == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso digitado foi {maior:.2f}kg e o menor peso digitado foi {menor:.2f}kg.')

