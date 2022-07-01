# crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços, na sequencia
# no final, mostre uma listagem de preços, organizando os dados em forma tabular.

lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
        'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for c in range(0, len(lista), 2):
    print(f'{lista[c]:.<30} R$ {lista[c+1]:6.2f}')
