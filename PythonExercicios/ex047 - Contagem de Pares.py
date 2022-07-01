# crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50

# no código abaixo o cpu vai calcular todos os números de 0 até 50.
for c in range(0, 51):
    if c % 2 == 0:
        print(c, end=' ')
print('Fim.')


# no código abaixo o cpu vai calcular apenas 1/2 dos números de 0 até 50, ocupando 1/2 do tempo do seu processador

for c in range(0, 51, 2):
    print(c, end=',')
print('Fim.')