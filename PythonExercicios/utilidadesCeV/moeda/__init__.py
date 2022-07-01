# usado nos exercicios 107 até 112
# 107 / 109 adição do parametro form e if/else
def aumentar(n=0, i=0, form=False):
    res = n+(n*i/100)
    if form:
        return moeda(res)
    else:
        return res


def diminuir(n=0, i=0, form=False):
    res = n-(n*i/100)
    if form:
        return moeda(res)
    else:
        return res


def dobro(n=0, form=False):
    res = 2*n
    if form:
        return moeda(res)
    else:
        return res


def metade(n=0, form=False):
    res = n/2
    if form:
        return moeda(res)
    else:
        return res


# 108
def moeda(n=0, m='R$'):
    return f'{m}{n:.2f}'.replace('.', ',')


# 110
def resumo(x=0, a=0, d=0):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço analisado:":<20}{moeda(x)}\n'
          f'{"Dobro do preço:":<20}{dobro(x, True)}\n'
          f'{"Metade do preço:":<20}{metade(x, True)}\n'
          f'{a}{"% de aumento:":<18}{aumentar(x, a, True)}\n'
          f'{d}{"% de redução:":<18}{diminuir(x, d, True)}')
    print('-' * 30)



