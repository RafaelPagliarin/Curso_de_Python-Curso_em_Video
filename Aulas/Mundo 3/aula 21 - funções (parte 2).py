começamos a trabalhar com:
. interactive help
. docstrings
. argumentos opcionais
. escopo de variáveis
. retorno de resultados

############### INTERACTIVE HELP ###################

help() é uma função interna do python
vc abre o console do python, usa só help() e depois digita qual comando/etc vc quer ver o "manual".


############### DOCSTRINGS #########################

toda funcionalidade interna do python tem uma docstring. elas são os manuais
para as funções que nós mesmo criamos (customizados)
para criar sua docstring (manual da sua função) nós fazemos 3 aspas duplas e colocamos o manual lá dentro

def contador(i, f, p):
    """
     -> Faz uma contagem e mostra na tela.
     :param i: inicio da contagem
     :param f: fim da contagem
     :param p: passo da contagem
     :return: sem retorno
     Função criada por Rafael Pagliarin baseado no curso em video de Python do cursoemvideo.     
     """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('Fim!')

no exemplo acima caso vc de help(contador) o texto escrito em verde vai surgir como uma docstring e servir de manual para
a função customizada

################################## PARAMETROS OPCIONAIS ########################################

def somar(a, b, c=0):
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 2, 5)
somar(8, 4) #se não tivesse o c=0 lá em cima, quando eu tentasse dar um somar com 2 valores só iria dar erro.

# e nada impede de vc colocar todas as variáveis da função como opcionais:
# def somar(a=0, b=0, c=0):

################################ ESCOPO DE VARIÁVEIS/DECLARAÇÕES ######################################
é o local onde a variável existe, e onde não existe
variável de escopo global
variável de escopo local

variáveis do programa principal são variaveis globais, vão funcionar dentro das funções e basicamente todos os lugares

variáveis criadas dentro de funções são variáveis locais, não existindo fora daquela função. Como outras funções e/ou
no programa principal

também existe diferença de escopo para chamada de importação. da para importar global e importar local

==============================================================================================================
ps: se houver uma variavel com nome igual (uma global e outra local) [vou usar no exemplo a variável "a"]
se vc fizer uma alteração na variavel a local. a global a continua intacta.
Se você quiser alterar a global é necessário "chamar" a "global a"

def teste(b):
    global a # necessário quando você quiser usar o "a" lá do global.
    a = 8 #se não tiver a linha de cima é local, com a linha de cima vira global
    b += 4
    c = 2
    print(a) # 8
    print(b) #9
    print(c) #2


a = 5
teste(a)
print(a) # 5
print(b) #
print(c) # erro

################################## RETORNO DE VALORES #########################################################

# comando: return

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


resp = somar(3, 2, 5) #ou jogar dentro de um print

