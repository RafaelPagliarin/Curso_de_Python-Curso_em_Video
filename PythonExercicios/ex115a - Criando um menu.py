# crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples
# o sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas

from ex115pack.funcs import *
from time import sleep

while True:
    resposta = menu('Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema')
    if resposta == 1:
        layout('Opção 1')
    elif resposta == 2:
        layout('Opção 2')
    elif resposta == 3:
        layout('SAINDO DO SISTEMA...')
        break
    else:
        print('\033[31mErro! Digite uma opção válida!\033[m')
    sleep(2)

