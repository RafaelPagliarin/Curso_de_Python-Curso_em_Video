adicionando listas dentro de listas (listas compostas)

dados = list()
dados.append('Pedro')
dados.append(25)

dados = ['Pedro', 25]

pessoas = list()
pessoas.append(dados[:])
pessoas = [['Pedro', 25]]
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]


print(pessoas[0][0]) #Pedro
print(pessoas[1][1]) #19
print(pessoas[2][0]) #João
print(pessoas[1])    #['Maria', 19]

# os indices nesse tipo de lista