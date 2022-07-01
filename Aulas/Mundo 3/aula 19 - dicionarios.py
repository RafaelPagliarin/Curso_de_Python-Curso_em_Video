aula 19 - variáveis compostas (dicionários)

tudo aquilo que foi ensinado em tuplas pode ser aplicado em listas
e tudo oq foi ensinado em tuplas e listas pode ser aplicado em dicionários


dados = list() # declarar uma lista
dados.append('Pedro') #adicionar 'Pedro' à lista dados
dados.append(25) # adicionar '25' à lista dados
print(dados[0]) # Pedro
print(dados[1]) # 25

nas listas (como no exemplo acima) os indices são núméricos. Mas e se eu quiser ter indices literais?
para resolver isso, no python, temos os dicionários.

dados = dict()
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M' #no dicionário não existe append, então para adicionar novos elementos é só usar assim
del dados['idade'] #para remover é só usar o del, o python arrumará o dicionário

filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'}

print(filme.values()) #são os dados dentro das keys
print(filme.keys()) # são os indices
print(filme.items()) #é a combinação de dados e indices

podemmos usar esses exemplos acima para laços de repetição. igual o enumerate nas listas

for k, v in filme.items():
    print(f'O {k} é {v}')

podemos também usar tuplas, lista e dicionários juntos/ ao mesmo tempo

imagine o dicionário filme acima, dentro de uma lista

locadora = [{'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas' },
            {'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedon'},
            {'titulo': 'Matrix', 'ano': 1999, 'diretor': 'Wachowshi'}]

print(locadora[0]['ano']) #1977
print(locadora[2]['titulo']) #matrix