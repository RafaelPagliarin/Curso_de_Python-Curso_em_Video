# escreva um programa para aprovar o empréstimo bancária para a compra de uma casa.
# o programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

# calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negado.

valor_casa = float(input('Qual o valor do imóvel? R$'))
salario_comprador = float(input('Qual o salário mensal do comprador? R$'))
tempo_pagamento = float(input('Em quantos anos será pago? '))
print()
if 0.3*salario_comprador >= (valor_casa / (tempo_pagamento * 12)):
    print(f'Empréstimo aprovado! o valor da parcela será de R${(valor_casa / (tempo_pagamento * 12)):.2f} por'
          f' {(tempo_pagamento * 12)} meses.')

    print(f'As parcelas correspondem a {((valor_casa / (tempo_pagamento * 12)) * 100) / salario_comprador:.2f}%'
          f' do salário do comprador.')
else:
    print(f'Infelizmente o empréstimo não foi aprovado. O valor da parcela'
          f' (R${(valor_casa / (tempo_pagamento * 12)):.2f}) é superior a 30% do salário'
          f' do candidato (R${0.3 * salario_comprador})')



