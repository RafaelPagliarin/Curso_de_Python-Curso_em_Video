# escreva um programa para aprovar o empréstimo bancária para a compra de uma casa.
# o programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

# calcule o valor da prestação mensal, sabendo que ela não pode exceder 30%^do salário ou então o emprestimo será negado.

valorcasa = float(input('Qual o valor do imóvel? R$'))
salcomprador = float(input('Qual o salário mensal do comprador? R$'))
temppag = float(input('Em quantos anos será pago? '))
print()
if 0.3*salcomprador >= (valorcasa/(temppag*12)):
    print(f'Empréstimo aprovado! o valor da parcela será de R${(valorcasa/(temppag*12)):.2f} por {(temppag*12)} meses.')
    print(f'As parcelas correspondem a {((valorcasa/(temppag*12))*100)/salcomprador:.2f}% do salário do comprador.')
else:
    print(f'''Infelizmente o empréstimo não foi aprovado. O valor da parcela (R${(valorcasa/(temppag*12)):.2f})
é superior a 30% do salário do candidato (R${0.3*salcomprador})''')

