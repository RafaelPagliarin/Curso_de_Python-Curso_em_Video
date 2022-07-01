'''faça um programa que leia o nome completo de uma pessoa e mostre em seguida o primeiro e último nome separadamente.
ex: ana maria de souza
primeiro: ana
ultimo: souza'''

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()

print(f'Primeiro nome: {nome[0]} \n Último nome: {nome[len(nome)-1]}')
