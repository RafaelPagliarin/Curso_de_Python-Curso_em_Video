#escrava um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento
#para salários superiores a R$1250.00 , calcule um aumento de 10%
#para os inferiores ou iguais, o aumento é de 15%

sal = float(input('Digite o salário do funcionário: R$'))

if sal > 1250:
    print(f'Com o reajuste, o novo salário passa a ser R${sal*1.1:.2f}')
else:
    print(f'Com o reajuste, o novo salário passa a ser R${sal*1.15:.2f}')
