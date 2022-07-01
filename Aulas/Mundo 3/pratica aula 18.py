'''teste = list()
teste.append('Rafael')
teste.append(30)
galera = list()
#galera.append(teste) # aqui acabamos criando uma ligação entre as duas estruturas, e ao alterar uma delas, alteramos a segunda também.
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''

# =====================================================================================================================

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(p[1])
    print(f'{p[0]} tem {p[1]} anos de idade.')

# =====================================================================================================================

'''galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)'''

