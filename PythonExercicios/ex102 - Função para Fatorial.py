# crie um programa que tenha uma função fatorial() que receba dois parametros: o primeiro que indique o número a calcular
# e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de
# calculo do fatorial


def fatorial(num, show=False):
    """
    -> Função que calcula o fatorial de um número.
    :param num: valor a ser calculado o fatorial
    :param show: (opcional) verdadeiro ou falso para mostrar a calculo.
    :return: retorna o resultado do fatorial
    """
    f = 1
    print("-=" * 25)
    print(f'           \33[31mCalculando o Fatorial de {num}:\33[m')
    for c in range(num, 0, -1):
        if show:
            if c == 1:
                print(f'{c}', end=' = ')
            else:
                print(f'{c}', end=' x ')
        f *= c
    return f


# Programa Principal
n = int(input('Digite o valor para calculo de Fatorial: '))
while True:
    s = str(input('Deseja mostrar o calculo? [S/N]: ')).strip().upper()
    if s in 'S':
        show = True
        break
    elif s in 'N':
        show = False
        break
    else:
        print('Opção invalida.')

if show:
    print(fatorial(n, show))
else:
    print(f'                Resposta: {fatorial(n, show)}')
print("-=" * 25)

''' #meu código antigo, aprimorei para remover redundancia
    f = 1
    if show:
        print("-=" * 25)
        print(f'           \33[31mCalculando o Fatorial de {num}:\33[m')
        for c in range(num, 0, -1):
            if c == 1:
                print(f'{c}', end=' = ')
            else:
                print(f'{c}', end=' x ')
            f *= c
    else:
        for c in range(num, 0, -1):
            f *= c
    return f
    '''