# faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parametro e mostre uma
# mensagem com tamanho adaptável (as linhas de "viadagem" ficam do tamanho do texto escrito)

# Funções
def Cabeçalho(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)


# Programa Principal
menu = str(input('Digite o cabeçalho desejado: '))
print()
Cabeçalho(menu)
