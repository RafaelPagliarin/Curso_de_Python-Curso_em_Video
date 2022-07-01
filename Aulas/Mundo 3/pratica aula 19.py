'''pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas['peso'] = 98.5 #assim que faz para adicionar elementos no dicionário.
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.') # para enunciar a key aqui usamos aspas duplas, pq é aspas dentro de aspas... já tive q fazer antes

for k in pessoas.keys(): #pessoas.items() , etc # enumarate não funciona em dicionários
    print(k)'''

####################### criando dicionários dentro de listas #######################################################

'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])'''

#################################################################################################################

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # brasil.append(estado) >>> veja a obs abaixo
print(brasil)

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')

# no exemplo acima (no comando depois do #) existiria um problema,
# o print só vai mostrar os dados do ultimo estado digitado, pq acabamos fazendo um
# vinculo entre a lista e o dicionário. Para resolver isso, nas listas, usamos o [:], mas isso também não funciona em
# dicionários. Pois não se pode usar fateamento em dicionários. o correto é usar o .copy