# crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário quer continuar
# no final, mostre:
# qual é o total gasto na compra
# quantos produtos custam mais de R$1000
# qual  é o nome do produto mais barato.

produto_mais_barato = ' '
total_gasto = mais_de_mil = mais_barato = 0
while True:
    cont = ' '
    produto = str(input('Qual o produto? ')).strip()
    preço = int(input('Qual o preço: R$'))
    if mais_barato == 0 or mais_barato > preço:
        produto_mais_barato = produto
        mais_barato = preço
    if preço > 1000:
        mais_de_mil += 1
    total_gasto += preço

    while cont not in 'SN':
        cont = str(input('Deseja continuar?')).strip().upper()[0]
        if cont not in 'SN':
            print('não entendi')
    if cont == 'N':
        break
print(f'O total gasto na compra foi R${total_gasto:.2f}')
print(f'onde {mais_de_mil} produtos custaram mais de R$1000.00')
print(f'e o produto mais barato foi o {produto_mais_barato} por R${mais_barato}')
