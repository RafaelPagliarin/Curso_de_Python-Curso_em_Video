from ex115pack.funcs import *
from ex115pack.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt' # tem que estar na mesma pasta do projeto

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu('Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema')
    if resposta == 1:
        # Opção de listar o conteúdo do arquivo!
        lerarquivo(arq)
    elif resposta == 2:
        layout('Opção 2')
    elif resposta == 3:
        layout('SAINDO DO SISTEMA...')
        break
    else:
        print('\033[31mErro! Digite uma opção válida!\033[m')
    sleep(2)

