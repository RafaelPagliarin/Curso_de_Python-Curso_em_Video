'''num = [2,5,9,1]
num[2] = 3
#num[4] = 7 # não funciona, pois não existe uma posição [4]. para criar precisamos usar o append
num.append(7)
num.sort()
num.sort(reverse=True)
num.insert(2, 2)
num.remove(2) #procura o primeiro elemento 2 e remove, não remove todos
print(num)
print(f'Essa lista tem {len(num)} elementos.')

num.pop(2)
if 4 in num:
    num.remove(4)
print(num)
print(f'Essa lista tem {len(num)} elementos.')'''

#======================================================================================================================

'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for cont in range(0, 5):
    valores.append(int(input(f'Digite o {cont+1}º valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')'''

# ========================= peculiaridade do python em listas ==================================================
'''a = [2,3,4,7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# quando vc iguala uma lista na outra "b = a", o python está ligando as duas listas, logo uma alteração na a,
# vai alterar o b também.

a = [2,3,4,7]
b = a[:] # aqui ele copia todos os valores de dentro de a para b, já não vale o exemplo de cima
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''