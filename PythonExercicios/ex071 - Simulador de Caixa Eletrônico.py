# crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será o
# valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues

# obs : considere que o caixa possui cédulas de 50, 20, 10 e 1.
'''
print('-=' * 8)
print('Caixa Eletrônico')
print('-=' * 8)
valor = int(input('Qual valor deseja sacar? R$'))
x = valor
n50 = n20 = n10 = n01 = 0
while True:
    if (x // 50) >= 1:
        n50 = x // 50
        x = x % 50
        if x == 0:
            break
    elif (x // 20) >= 1:
        n20 = x // 20
        x = x % 20
        if x == 0:
            break
    elif (x // 10) >= 1:
        n10 = x // 10
        x = x % 10
        if x == 0:
            break
    elif (x // 1) >= 1:
        n01 = x // 1
        break

print(f'Você receberá R${valor} em {n50} notas de R$50, {n20} notas de R$20, {n10} notas de R$10 e {n01} notas de R$1')'''

# a resposta do guanabara foi tão diferente da minha que resolvi escreve-la aqui.

valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
