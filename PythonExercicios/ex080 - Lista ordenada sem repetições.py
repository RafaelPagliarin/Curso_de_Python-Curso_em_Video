# crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista, já na posição correta
# de inserção (sem usar o sort()).
# no final, mostre uma lista ordenada na tela

lista = []
for c in range(0, 5):
    valor = int(input(f'Digite o {c+1}º valor: '))
    if c == 0 or (valor > lista[-1]):
        lista.append(valor)
        print('Adicionado valor ao final da lista...')
    else:
        for x in range(len(lista)):
            if valor <= lista[x]:
                lista.insert(x, valor)
                print(f'Adicionado valor na posição {x+1} da lista')
                break
print('-=' * 30)
print(f'Os valores digitados em ordem foram: {lista}')
