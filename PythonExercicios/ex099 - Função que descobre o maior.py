# faça um programa que tenha uma função chamada maior(), que receba vários parametros com valores inteiros
# seu programa tem que analisar todos os valores e dizer qual deles é o maior

from time import sleep


def maior(* num):
    print("-=" * 20)
    print('Analisando os valores passados...')
    sleep(1)
    print(num)
    for v, k in enumerate(num):
        for i in range(0, len(k)):
            if i == 0:
                m = k[0]
            else:
                if k[i] > m:
                    m = k[i]
    print(f'O maior valor digitado foi {m}.')


lista = list()
while True:
    lista.append(int(input('Digite um número inteiro: ')))
    while True:
        cont = str(input('Deseja continuar? [S/N]: ')).strip().upper()
        if cont in 'SN':
            break
        print('Opção inválida.')
    if cont == 'N':
        break
print(lista)
maior(lista)
