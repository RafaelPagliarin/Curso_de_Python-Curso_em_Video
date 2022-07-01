# aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
# do aproveitamento de cada jogador.

jogador = dict()
elenco = list()
lista_gols = list()
gols = acumulado = 0

while True:
    lista_gols.clear()
    jogador.clear()
    jogador['Nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for x in range(0, partidas):
        gols = (int(input(f'Quantos gols {jogador["Nome"]} fez no {x + 1}º jogo? ')))
        acumulado += gols
        lista_gols.append(gols)
    jogador['Gols por partida'] = lista_gols[:]
    jogador['Total'] = acumulado
    elenco.append(jogador.copy())
    while True:
        cont = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if cont in 'SN':
            break
        print('Opção inválida.')
    if cont == 'N':
        print('encerrando cadastros...')
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<20}', end='')
print()
print('-' * 45)
for k, v in enumerate(elenco):
    print(f'{k:<3}', end='')
    for i in v.values():
        print(f'{str(i):<20} ', end='')
    print()
print('-' * 45)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(elenco):
        print(f'Erro! Não existe jogador com código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR: {elenco[busca]["Nome"]}')
        for i, g in enumerate(elenco[busca]['Gols por partida']):
            print(f'      No {i+1}º jogo fez {g} gols.')
    print('-' * 45)
print('<< VOLTE SEMPRE >>')
