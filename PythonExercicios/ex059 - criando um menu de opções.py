#crie um programa que leia dois valores e mostre um menu na tela:

# 1 somar
# 2 multiplicar
# 3 maior
# 4 novos números
# 5 sair do programa

# seu programa deverá realizar a operação solicitada em cada caso

option = ''
while option != 5:
    print()
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    option = ''
    while option != 4 and option != 5:
        print('-=' * 20)
        print('''    [1] somar os valores digitados 
    [2] multiplicar os valores digitados
    [3] descobrir qual valor é maior
    [4] digitar novos valores
    [5] sair ''')
        print('-=' * 20)
        option = int(input('Digite a opção desejada: '))

        if option == 1:
            print(f'{n1} + {n2} = {n1+n2}.')
        elif option == 2:
            print(f'{n1} x {n2} = {n1*n2}.')
        elif option == 3:
            if n1 > n2:
                print(f'O maior valor é {n1}.')
            elif n1 == n2:
                print(f'Os valores digitados são iguais.')
            else:
                print(f'O maior valor é {n2}.')
        elif option == 5:
            print('Saindo...')
