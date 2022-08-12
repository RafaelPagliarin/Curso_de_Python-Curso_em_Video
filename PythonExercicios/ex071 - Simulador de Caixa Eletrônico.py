# crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será o
# valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues

# obs : considere que o caixa possui cédulas de 50, 20, 10 e 1.

valor = int(input('Que valor você quer sacar? R$'))
total = valor
nota_atual = 50
total_notas = 0
while True:
    if total >= nota_atual:
        total -= nota_atual
        total_notas += 1
    else:
        if total_notas > 0:
            print(f'Total de {total_notas} cédulas de R${nota_atual}')
        if nota_atual == 50:
            nota_atual = 20
        elif nota_atual == 20:
            nota_atual = 10
        elif nota_atual == 10:
            nota_atual = 1
        total_notas = 0
        if total == 0:
            break
