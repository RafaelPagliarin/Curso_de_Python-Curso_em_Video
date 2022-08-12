# faça um programa que mostre a tabauada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# o programa será interrompido quando o número solicitado for negativo.


while True:
    tabuada = int(input('Valor da tabuada desejada: '))
    if tabuada <= 0:
        print('Encerrando Programa de Tabuada...')
        break
    for x in range(0, 11):
        print(f'{tabuada} x {x:0>2} = {tabuada * x:0>2}')

    print()


