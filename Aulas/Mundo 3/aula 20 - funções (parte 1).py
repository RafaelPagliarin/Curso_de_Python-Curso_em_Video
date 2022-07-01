funções estão ligadas a rotinas (algo que se faz constantemente)

print() , len(), input(), int(), float() são funções... por exemplo, porem são funções já existentes no python

def é o termo usado para definição de função, é o que usamos para criar/chamar(?) funções:

O Guanabara, por exemplo, sempre cria linhas trassejadas para separar titulos, textos, etc. Essas linhas podem ser convertidas
em uma função (rotina) e isso facilia sua vida.

def mostraLinha():
    print('-------------------------------------------------------')


============================= exemplo sem função ===============================

print('-------------------------------------------------------')
print('                   SISTEMA DE ALUNOS                   ')
print('-------------------------------------------------------')
print('-------------------------------------------------------')
print('                 CADASTRO DE FUNCIONÁRIOS              ')
print('-------------------------------------------------------')
print('-------------------------------------------------------')
print('                    ERRO DO SISTEMA                    ')
print('-------------------------------------------------------')

============================= exemplo com função ===============================

mostraLinha
print('                   SISTEMA DE ALUNOS                   ')
mostraLinha
mostraLinha
print('                 CADASTRO DE FUNCIONÁRIOS              ')
mostraLinha
mostraLinha
print('                    ERRO DO SISTEMA                    ')
mostraLinha

ps: o pycharm pede que entre suas funções e seu programa principal tenham 2 linhas vazias, por questões estéticas.
ps: toda função exige " (): " no final

o def cria funções customizadas. ele também pode ser usado com parametros.

==================================== EXEMPLO COM PARAMETROS ====================================================

def mensagem(msg):
print('-------------------------------------------------------')
print(msg)
print('-------------------------------------------------------')


mensagem('SISTEMA DE ALUNOS')

