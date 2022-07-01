# crie um programa que leia nome e 2 notas de vários alunos e guarde tudo em uma lista composta.
# no final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
# individualmente
from time import sleep
aux = list()
boletim = list()
while True:
    c = ' '
    nome = str(input('Digite o nome: '))
    p1 = float(input('Digite a nota da P1 '))
    p2 = float(input('Digite a nota da P2: '))
    m = (p1+p2)/2
    aux = [nome, p1, p2, m]
    boletim.append(aux[:])
    aux.clear()
    while c not in 'SN':
        c = str(input('Deseja continuar? ')).strip().upper()[0]
        if c not in 'SN':
            print('Não entendi.')
    if 'N' in c:
        print('Encerrando adição de notas...')
        break

while True:
    c = ' '
    print(f'{"Número":>6} {"Nome":^20} {"Média":5}')
    for c, v in enumerate(boletim):
        print(f'{c:>6} {v[0]:.<20} {v[3]:5}')
    x = int(input('Gostaria de ver as notas de qual aluno? [999 para encerrar] : '))
    if x == 999:
        print('Até mais...')
        break
    else:
        print(f'As notas do aluno {boletim[x][0]} foram {boletim[x][1]} e {boletim[x][2]}.\n')
        sleep(2)


