semelhantes as tuplas,

tupla >>>> lanche('burguer', 'suco', 'pizza', 'pudim')
lista >>>> lanche['burguer', 'suco', 'pizza', 'pudim']

as listas podem ser mutáveis, logo é possível alterar elementos dentro de uma lista existente.

tanto tuplas quanto listas guardam valores de forma quase iguais.

# adicionando itens à listas
lanche.append('cookie') # adicionar cookie ao final da lista lanche
lanche.insert(0,'cachorro quente') # adiciona uma posição no zero (que já existia) e coloca o cachorro quente lá

# removendo itens de listas
del lanche[3]
lanche.pop(3) # o pop normalmente é usado sem nada no parametro para remover o último elemento da lista
lanche.remove('pizza') # o remove usa o nome do elemento e não sua posição

quando removemos um item no meio da lista, o python reposiciona os indices dos itens dentro da lista automaticamente.

caso queria verificar se existe algo na lista antes de remover
é importante pois caso vc tente remover algo q não existe, a linguagem dará um erro.

if 'pizza' in lanche:
    lanche.remove('pizza')

# criando listas usando comando list
valores = list(range(4,11))

# mudando ordem da lista
valores = [8,2,5,4,9,3,0]
valores.sort() >>> 0,2,3,4,5,8,9
valores.sort(reverse=True) >>> 9,8,5,4,3,2,0

# tamanho da lista
len(valores) >>> 7