# faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

algo = input('Digite algo: ')
# prints no modo "antigo" (python 3.0)
print('O tipo primitivo desse valor é: ', type(algo))
print('Só tem espaços?',algo.isspace())
print('O que você digitou é numérico?', algo.isnumeric())
print('O que você digitou é alfabético?', algo.isalpha())
print('O que você digitou é alfanumérico?' , algo.isalnum())
print('O que você digitou está tudo em maiusculo?', algo.isupper())
print('O que você digitou está tudo em minusculo?', algo.islower())
print('O que você digitou está capitalizado?', algo.istitle())
# prints no modo "novo" (python ~3.7 diante)
#print(f'O tipo primitivo desse valor é {type(algo)}')
#print(f'Só tem espaços? {algo.isspace()}')

