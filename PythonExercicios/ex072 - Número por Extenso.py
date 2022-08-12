# crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte
# seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostra-lo por extenso.

numextenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
              'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    cont = ' '
    while True:
        num = int(input('Digite um número de 0 à 20: '))
        if 0 <= num <= 20:
            break
        print('Valor inválido, tente novamente.')
    print(f'O número digitado foi \33[31m{numextenso[num]}\33[m')

    while cont not in 'SN':
        cont = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
        if cont not in 'NS':
            print('Opção inválida')
    if cont in 'N':
        print('Encerrando')
        break
