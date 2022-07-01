# crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário quer continuar
# no final, mostre:
# qual é o total gasto na compra
# quantos produtos custam mais de R$1000
# qual  é o nome do produto mais barato.

baratonome = ' '
tot = caro = barato = 0
while True:
    cont = ' '
    produto = str(input('Qual o produto? ')).strip()
    price = int(input('Qual o preço: R$'))
    if barato == 0 or barato > price:
        baratonome = produto
        barato = price
    if price > 1000:
        caro += 1
    tot += price

    while cont not in 'SN':
        cont = str(input('Deseja continuar?')).strip().upper()[0]
        if cont not in 'SN':
            print('não entendi')
    if cont == 'N':
        break
print(f'O total gasto na compra foi R${tot:.2f}')
print(f'onde {caro} produtos custaram mais de R$1000.00')
print(f'e o produto mais barato foi o {baratonome} por R${barato}')
