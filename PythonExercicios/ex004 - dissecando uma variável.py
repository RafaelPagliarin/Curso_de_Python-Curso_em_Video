# faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

texto = input('Digite algo: ')

print(f'O tipo primitivo do que foi digitado é: {type(texto)} ')
print(f'Só tem espaços? {texto.isspace()}')
print(f'O que você digitou é numérico? {texto.isnumeric()}')
print(f'O que você digitou é alfabético? {texto.isalpha()}')
print(f'O que você digitou é alfanumérico? {texto.isalnum()}')
print(f'O que você digitou está tudo em maiusculo? {texto.isupper()}')
print(f'O que você digitou está tudo em minusculo? {texto.islower()}')
print(f'O que você digitou está capitalizado? {texto.istitle()}')

