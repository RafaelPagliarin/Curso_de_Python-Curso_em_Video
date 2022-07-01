# crie um programa que leia vários números inteiros pelo teclado. no final da execução, mostre a média entre todos os valores
# e qual foi o maior e menor valor lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

x = 0
c = 0
cont = 'S'

while cont == 'S':
    n = int(input('Digite um valor: '))
    if c == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    x += n
    c += 1
    cont = ''

    while cont != 'S' and cont != 'N':
        cont = str(input('Deseja continuar? [S/N]: ')).strip().upper()
        if cont != 'S' and cont != 'N':
            print('Não entendi, responda novamente.')
print()
print(f'O maior valor digitado foi {maior}, o menor valor digitado foi {menor} e a média entre os {c} valores digitados'
      f' é {x/c}')


