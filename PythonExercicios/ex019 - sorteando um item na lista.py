# um professor quer sortear um dos seus quatro alunos para apagar o quadro. faça um programa que ajude ele,
# lendo o nome deles e escrevevendo o nome do escolhido.

from random import choice
aluno1 = input('Qual o nome do 1º aluno : ')
aluno2 = input('Qual o nome do 2º aluno : ')
aluno3 = input('Qual o nome do 3º aluno : ')
aluno4 = input('Qual o nome do 4º aluno : ')
lista = [aluno1, aluno2, aluno3, aluno4]
print()
print(f'O aluno que apagará o quadro é {choice(lista)}')