# crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do python,
# só que fazendo a validação para aceitar apenas um valor numérico.
# ex:
# n = leiaInt('Digite um n')


def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg)).replace(',', '.')
        if n.isnumeric():
            valor = float(n)
            ok = True
        else:
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


# Programa Principal
x = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {x}')

