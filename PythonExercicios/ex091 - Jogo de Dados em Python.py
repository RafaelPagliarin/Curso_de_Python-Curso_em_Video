# crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from time import sleep
from random import randint
from operator import itemgetter

# criando dict com a jogada dos 4 jogadores
res = {'jogador 1': randint(1, 6),
       'jogador 2': randint(1, 6),
       'jogador 3': randint(1, 6),
       'jogador 4': randint(1, 6)}

print('=-' * 15)
# printando os resultados
print(f'{"Valores Sorteados":^30}')
for k, v in res.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)
# criando lista ordenada
ranking = sorted(res.items(), key=itemgetter(1), reverse=True)
#printando o ranking ordenado
print('=-' * 15)
print(f'{"RANKING DOS JOGADORES":^30}')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(0.5)
print('=-' * 15)

