cfun = ('\033[m',  # 0 - sem cor
        '\033[0;97;40m',  # 1 - preto
        '\033[0;97;41m',  # 2 - vermelho
        '\033[0;97;42m',  # 3 - verde
        '\033[0;97;43m',  # 4 - amarelo
        '\033[0;97;44m',  # 5 - azul
        '\033[0;97;45m',  # 6 - magenta
        '\033[0;97;46m',  # 7 - ciano
        '\033[0;97;47m',  # 8 - cinza
        '\033[0;30;107m'  # 9 - branco
        )

ctxt = ('\033[m',  # 0 - sem cor
        '\033[1;30m',  # 1 - preto
        '\033[1;31m',  # 2 - vermelho
        '\033[1;32m',  # 3 - verde
        '\033[1;33m',  # 4 - amarelo
        '\033[1;34m',  # 5 - azul
        '\033[1;35m',  # 6 - magenta
        '\033[1;36m',  # 7 - ciano
        '\033[1;37m',  # 8 - vermelho
        '\033[1;97m'   # 9 - branco
        )


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def layout(msg):
    from random import randint
    y = randint(0, 9)
    x = randint(0, 9)
    while x == y:
        x = randint(0, 9)
    print(cfun[y], ctxt[x], '-' * 60, cfun[0], ctxt[0])
    print(cfun[y], ctxt[x], f'{msg:^60}', cfun[0], ctxt[0])
    print(cfun[y], ctxt[x], '-' * 60, cfun[0], ctxt[0])


def menu(*lista):
    # while True:
    layout('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(ctxt[3], c, ctxt[0], '-', ctxt[5], item, ctxt[0])
        c += 1
    op = leiaint('Sua opção: ')
    return op
