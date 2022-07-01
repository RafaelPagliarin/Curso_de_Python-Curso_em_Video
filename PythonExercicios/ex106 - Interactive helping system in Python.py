# faça um mini-sistema que utilize o interactive help do python. O usuário vai digitar o comando e o manual vai aparecer
# quando o usuário digitar a palavra "FIM", o programa vai ser encerrado.
# obs: use cores.

from time import sleep
# tupla com cores, para facilitar
c = ('\033[m',  # 0 - sem cor
     '\033[0;97;41m',  # 1 - vermelho
     '\033[0;97;42m',  # 2 - verde
     '\033[0;97;43m',  # 3 - amarelo
     '\033[0;97;44m',  # 4 - azul
     '\033[0;97;45m',  # 5 - magenta
     '\033[0;97;46m',  # 6 - ciano
     '\033[0;30;107m'  # 7 - branco
     )


def ajuda(n):
    título(f'Acessando o manual do comando \'{n}\'', 4) #usando \' para colocar aspas dentro de aspas, quando algo é proibido de ser colocado em uma string
    print(c[7], end='')
    print(help(n))
    print(c[0], end='')
    sleep(1)


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# Programa Principal
manual = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    manual = str(input('Função ou Biblioteca [FIM para encerrar]: ')).strip().upper()
    if manual == 'FIM':
        break
    else:
        ajuda(manual.lower())
título('ATÉ LOGO!', 1)
