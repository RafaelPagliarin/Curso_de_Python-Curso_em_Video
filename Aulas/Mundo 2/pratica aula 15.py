'''cont = 1
while True: # executa tudo dentro do while para sempre, até apertar stop ou usar o comando break
    print(cont, '...', end='')
    cont += 1
print('acabou')'''

# ===========================================================
n = s = 0
while n != 999: #aqui estamos usando o 999 como "flag" para finalização
    n = int(input('Digite um número: '))
    s += n
print(f'A soma vale {s}')

# no exemplo acima, como usamos o 999 como flag, a soma vai incluir o 999... é possível corrigir isso com "gambiarras"
# por exemplo, diminuir 999 da soma total. mas é gambiarra
# o modo mais correto para resolver isso é usando o break, como abaixo:

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')

