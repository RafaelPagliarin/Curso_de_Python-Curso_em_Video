# escreva um programa que leia 2 números inteiros e compare-os, mostrando na tela a seguinte mensagem:
# - o primeiro valor é maior
# - o segundo valor é maior
# - não existe valor maior, os dois são iguais

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print()
if n1 == n2:
    print('Não existe valor maior, os dois são iguais!')
elif n1 > n2:
    print('O primeiro valor é maior.')
else:
    print('O segundo valor é maior.')
