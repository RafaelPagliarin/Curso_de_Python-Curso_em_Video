cfun = ('\033[m',         # 0 - sem cor
            '\033[0;97;41m',  # 1 - vermelho
            '\033[0;97;42m',  # 2 - verde
            '\033[0;97;43m',  # 3 - amarelo
            '\033[0;97;44m',  # 4 - azul
            '\033[0;97;45m',  # 5 - magenta
            '\033[0;97;46m',  # 6 - ciano
            '\033[0;30;107m'  # 7 - branco
            )

ctxt = ('\033[m',         # 0 - sem cor
          '\033[1;31;40m',  # 1 - vermelho
          '\033[1;32;40m',  # 2 - verde
          '\033[1;33;40m',  # 3 - amarelo
          '\033[1;34;40m',  # 4 - azul
          '\033[1;35;40m',  # 5 - magenta
          '\033[1;36;40m',  # 6 - ciano
          '\033[1;97;40m'   # 7 - branco
          )



from time import sleep
from random import randint
x = randint(0, 7)
print(corfundo[x], '-' * 60, corfundo[0])
print(f'{"TESTE":^60}')
print('-' * 60)
