'''22 - analisador de textos
crie um programa que leia o nome completo de uma pessoa e mostre:
o nome com todas as letras maiusculas
o nome com todas minusculas
quantas letras ao todo (sem considerar espaços)
quantas letras tem o primeiro nome'''

nome = input('Digite seu nome completo ')
lista_nome = nome.split()
nomejunto = ''.join(lista_nome)
print()
print(f'Nome digitado: {nome}')
print(f'Nome com letras maiusculas: {nome.upper()}')
print(f'Nome com letras minusculas: {nome.lower()}')
print(f'quantas letras o nome completo possui: {len(nome)}')
print(f'quantas letras o nome completo possui sem espaços: {len(nome) - nome.count(" ")}') # duas opções aqui
print(f'quantas letras o nome completo possui sem espaços: {len(nomejunto)}') # duas opções aqui
print(f'quantas letras possui o primeiro nome: {len(lista_nome[0])}')
print(lista_nome)
print(nomejunto)









