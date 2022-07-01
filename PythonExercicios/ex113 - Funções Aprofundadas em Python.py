# Reescreva a função leiaint() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número
# do tipo inválido. Aproveite e crie também uma função leiafloat() com a mesma funcionalidade.

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


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


# Programa Principal
x = leiaint('Digite um número inteiro: ')
y = leiafloat('Digite um número real: ')
print(f'Você acabou de digitar o número inteiro {x} e o real {y}.')
