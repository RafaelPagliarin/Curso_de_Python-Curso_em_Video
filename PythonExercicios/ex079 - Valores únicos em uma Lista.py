# crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista.
# caso o número já exista lá dentro, ele não será adicionado.
# no final, serão exibidos todos os valores únicos digitados, em ordem crescente.


lista = []
while True:
    cont = ' '
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
    while cont not in 'NS':
        cont = str(input('Continuar? [S/N]')).strip().upper()[0]
        if cont not in 'NS':
            print(f'Não entendi...')
    if cont in 'N':
        break
lista.sort()
print(lista)
