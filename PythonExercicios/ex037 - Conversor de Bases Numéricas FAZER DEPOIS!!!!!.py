# escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 binário
# 2 octal
# 3 hexadecimal

# bases númericas é algo bem importante, mas não aprendemos nesse curso (ainda?) - pesquisar na internet como funciona
# talvez deixar para depois???

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
option = int(input('Sua opção: '))

if option == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}') # lembrando que o "[2:]" é sobre fatiamento de string, aula 10
elif option == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif option == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção Inválida')
