#elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento

# a vista dinheiro/cheque: 10% de desconto
# a vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais: 20% de juros

price = float(input('Digite o preço do produto: R$'))
print('-=-' * 10)
print('''     OPÇÕES DE PAGAMENTO:

1. A vista dinheiro/cheque
2. A vista no cartão
3. Crédito até 2x
4. Crédito 3x ou mais''')
print('-=-' * 10)
modo = int(input('Modo de pagamento desejado: '))
print()
if (modo == 3) or (modo == 4):
    print('Crédito selecionado!')
    parcelas = int(input('Em quantas parcelas deseja pagar? '))
print()
if modo == 1:
    print(f'Pagamento à vista no dinheiro/cheque possui um desconto de 10%! Sua compra ficou em R${price*0.9}')
elif modo == 2:
    print(f'Pagamento à vista no cartão possui desconto de 5%! Sua compra ficou em R${price*0.95}')
elif modo == 3:
    print(f'Pagamento no crédito em até 2x não possui desconto. Sua compra ficou em {parcelas} parcelas de {price/parcelas}')
elif modo == 4:
    print(f'Pagamento no crédito em mais de 3x possui 20% de juros. Sua compra ficou em {parcelas} parcelas de {(price*1.2)/parcelas}')

