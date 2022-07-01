# faça um programa que tenha uma função chamada ficha(), que receba dois parametros opcionais: o nome de um jogador e
# quantos gols ele marcou

# o programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente


def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez um total de {gols} gol(s) no campeonato.')


#Programa Principal
j = ' '
j = str(input('Digite o nome do jogador: '))
g = str(input(f'Quantos gols o jogador {j} fez?'))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if j.strip() == '':
    ficha(gols=g)
else:
    ficha(j, g)

