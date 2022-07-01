# crie uma tupla preenchida com os 20 primeiros colocados na tabela do brasileirão, na ordem de colocação. depois mostre:
# a) apenas os 5 primeiros colocados.
# b) os ultimos 4 colocados na tabela.
# c) uma lista com os times em ordem alfabética
# d) em que posição na tabela está o time da chapecoense

brasileiro = ('Corinthians', 'Palmeiras', 'São Paulo', 'Atlético-MG', 'Botafogo', 'Santos', 'Fluminense', 'Coritiba',
              'América-MG', 'Avaí', 'Internacional', 'Athletico-PR', 'Bragantino', 'Flamengo', 'Goiás', 'Cuiabá',
              'Atlético-GO', 'Juventude', 'Ceará', 'Fortaleza')

print(brasileiro)
print('-=' * 40)
print('Os 5 primeiros:')
print(f'{brasileiro[:5]}')
print('-=' * 40)
print('Os 4 últimos:')
print(f'{brasileiro[-4:]}')
print('-=' * 40)
print(f'{sorted(brasileiro)}')
print('-=' * 40)
print(f'O Avaí está na {brasileiro.index("Avaí")+1}ª posição')

