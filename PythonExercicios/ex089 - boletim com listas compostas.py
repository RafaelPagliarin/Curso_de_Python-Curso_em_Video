# crie um programa que leia nome e 2 notas de vários alunos e guarde tudo em uma lista composta.
# no final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
# individualmente
from time import sleep
lista_boletim = list()

# criação da lista com nome e notas
while True:
    continuar = ' '
    nome = str(input('Digite o nome: '))
    p1 = float(input('Digite a nota da P1 '))
    p2 = float(input('Digite a nota da P2: '))
    media = (p1 + p2) / 2
    lista_aux = [nome, p1, p2, media]
    lista_boletim.append(lista_aux[:])
    lista_aux.clear()
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? ')).strip().upper()[0]
        if continuar not in 'SN':
            print('Não entendi.')
    if 'N' in continuar:
        print('Encerrando adição de notas...')
        break

# apresentação visual da lista criada
while True:
    continuar = ' '
    print(f'{"Código":>6} {"Nome":^20} {"Média":5}')
    for index, valor in enumerate(lista_boletim):
        print(f'{index:^6} {valor[0]:.<20} {valor[3]:5}')
    aluno_na_lista = int(input('Digite o código do aluno que gostaria de ver as notas detalhadas?'
                               ' [999 para encerrar] : '))
    if aluno_na_lista == 999:
        print('Até mais...')
        break
    else:
        print(f'As notas do aluno {lista_boletim[aluno_na_lista][0]} foram {lista_boletim[aluno_na_lista][1]}'
              f' e {lista_boletim[aluno_na_lista][2]}.\n')
        sleep(2)


