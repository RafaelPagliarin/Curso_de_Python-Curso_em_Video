# crie um programa que gerencie o aproveitamento de um jogador de futebol, o programa vai ler o nome do jogador e quantas
# partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um
# dicionário, incluindo o total de gols feitos durante o campeonato.
jogadores = dict()
gols = acumulado = 0
lista_gols = list()
jogadores['nome'] = str(input('Nome do Jogador: '))
jogadores['partidas'] = int(input(f'Quantas partidas {jogadores["nome"]} jogou? '))
for x in range(0, jogadores['partidas']):
    gols = (int(input(f'Quantos gols {jogadores["nome"]} fez no {x + 1}º jogo? ')))
    acumulado += gols
    lista_gols.append(gols)
jogadores['gols por partida'] = lista_gols[:]
jogadores['total'] = acumulado

print('-=' * 20)
print(f'O jogador {jogadores["nome"]} jogou {jogadores["partidas"]} partidas.')
for i, v in enumerate(jogadores["gols por partida"]):
    print(f'   => Na partida {i+1}, fez {v} gols.')
print(f'Totalizando {jogadores["total"]} gols.')