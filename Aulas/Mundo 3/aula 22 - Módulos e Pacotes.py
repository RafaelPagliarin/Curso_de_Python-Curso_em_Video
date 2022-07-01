# modularização - surgiu no início dos anos 60, onde os sistemas ficavam cada vez maiores.
# foco é dividir um programa grande e aumentar a legibilidade, facilitando a manutenção
# a ideia é dividir um problemão em pequenos problemas

def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f


num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')


# criamos um 3º projeto chamado Modulos, e lá estamos aprendendo a criar os módulos. basicamente o python consegue
# enxergar qualquer arquivo .py como um módulo, desde q tenha funções lá dentro
# para isso usamos o import, igual para os módulos pré instalados no python
# a diferença é que usamos "import arquivo_py" e para cada função temos q colocar arquivo_py.função
# mesma coisa para quando importamos a biblioteca/modulo inteiro, ao invés de importar apenas a função especifica

# import time
# from time import sleep

# mas da para fazer "from uteis import fatorial"
# mas o python não recomenda fazer isso para bibliotecas customizadas, pq pode dar conflito (ter duas funções com mesmo nome)
# na pratica a ultima a ser importada é a que vai ser utilizada, mas da b.o.


# vantagens
organização do código
facilidade na manutenção
ocultação do código detalhado
reutilização em outros projetos

#################################### PACOTES (outras lingaguens chamam isso de biblioteca) ############################

uma pasta que contem modulos (ao invés de criar vários modulos)

imagine que dentro de "uteis" (um pacote) existam vários modulos, um para números, outro para strings, outro para datas
outro para cores

para importar:

import uteis
from uteis import datas

dentro do python toda pasta dentro de um projeto pode ser um pacote
da mesma forma que todo arquivo py pode ser um modulo

existe uma sintase para uso, o pycharm cria o arquivo automaticamente (__init__.py)

dentro do projeto criamos um tipo de arquivo chamado "python package" (que será o pacote)
dentro desse pacote, podem haver outros pacotes. e em cada pacote haverá o arquivo .py criado automaticamente pelo pycharm
__init__ e é dentro dele que colocamos as funções

projeto > python package > __init__.py > função

e na hora de importar, vamos importar assim
from uteis import numeros
uteis é um pacote e numeros é um modulo (e não uma função)
e na hora de usar uma função de numeros usamos numeros.função (igual quando chamamos só import modulo)
é como se usassemos uma pasta a mais na hora de chamar a função