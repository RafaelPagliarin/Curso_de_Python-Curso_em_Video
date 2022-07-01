# faça um programa que mostre a tabauada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# o programa será interrompido quando o número solicitado for negativo.


while True:
    i = int(input('Valor da tabuada desejada: '))
    if i < 0:
        print('Encerrando Programa de Tabuada...')
        break
    for x in range(1, 11):
        print(f'{i} x {x:0>2} = {i*x:0>2}')

    print()


