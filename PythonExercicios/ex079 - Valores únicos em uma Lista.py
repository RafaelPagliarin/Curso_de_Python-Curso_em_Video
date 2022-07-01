# crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista.
# caso o número já exista lá dentro, ele não será adicionado.
# no final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
while True:
    cont = ''
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
    cont = str(input('Continuar? ')).strip().upper()
    if cont in 'NÃO':
        break

lista.sort()
print(lista)
