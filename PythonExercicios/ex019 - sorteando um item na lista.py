# um professor quer sortear um dos seus quatro alunos para apagar o quadro. faça um programa que ajude ele,
# lendo o nome deles e escrevevendo o nome do escolhido.

from random import choice
a1 = input('Qual o nome do 1º aluno : ')
a2 = input('Qual o nome do 2º aluno : ')
a3 = input('Qual o nome do 3º aluno : ')
a4 = input('Qual o nome do 4º aluno : ')
lista = [a1, a2, a3, a4]
print()
print(f'O aluno que apagará o quadro é {choice(lista)}')
