# faça um programa que leia um número qualquer e mostre seu fatorial
print('-=' * 12)
print('Calculadora de Fatorial')
print('-=' * 12)
numero = int(input('Digite um número: '))
contador = 1
resultado = 1
while numero >= contador:
    resultado *= contador
    if contador == 1:
        print(f'{numero}! = {contador}', end=' x ')
    elif contador == numero:
        print(f'{contador} = {resultado}')
    else:
        print(f'{contador}', end=' x ')
    contador += 1

# ======== usando o "factorial" =============
# fatorial = factorial(n)
# print(f'O fatorial de {numero}! é {fatorial}')
