# crie um programa que leia vários números inteiros pelo teclado. no final da execução, mostre a média entre todos os valores
# e qual foi o maior e menor valor lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

somatorio = 0
contador = 0
continuar = 'S'

while continuar == 'S':
    valor = int(input('Digite um valor: '))
    if contador == 0:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor
        elif valor < menor:
            menor = valor
    somatorio += valor
    contador += 1
    continuar = ''

    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
        if continuar != 'S' and continuar != 'N':
            print('Não entendi, responda novamente.')
print()
print(f'O maior valor digitado foi {maior}, o menor valor digitado foi {menor} e a média entre os {contador} valores digitados'
      f' é {somatorio / contador}')


