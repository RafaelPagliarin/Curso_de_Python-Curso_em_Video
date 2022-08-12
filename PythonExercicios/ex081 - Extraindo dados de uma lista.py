# crie um programa que vai ler vários números e colocar em uma lista.
# depois disso, mostre:
# a) quantos números foram digitados
# b) a lista de valores, ordenada de forma decrescente
# c) se o valor 5 foi digitado e está ou não na lista.
lista = []
while True:
    cont = ' '
    try:
        lista.append(int(input('Digite um número: ')))
    except(ValueError):
        print('Erro no tipo digitado')
    while cont not in 'SN':
        cont = str(input('Continuar? [S/N] ')).strip().upper()[0]
        if cont not in 'SN':
            print('Resposta inválida')
    if 'N' in cont:
        break
print('-=' * 20)
print(f'Foram digitados {len(lista)} valores.')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print(f'o número 5 foi digitado.')
else:
    print('o número 5 não foi digitado.')
print('-=' * 20)
