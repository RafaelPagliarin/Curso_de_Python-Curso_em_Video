# desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# a) quantas vezes apareceu o valor 9
# b) em que posição foi digitado o primeiro 3
# c) quais foram os números pares.

num = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')),
       int(input('Digite um número: ')))

print(f'Os valores digitados foram: {num}')

print(f'O número 9 aparece {num.count(9)} vezes')
if 3 in num:
    print(f'O primeiro número 3 foi digitado na posição {(num.index(3))+1}')
else:
    print('O número 3 não foi digitado.')
print(f'Os números pares digitados foram: ', end='')
for c in range(0, 3):
    if num[c] % 2 == 0:
        print(f'{num[c]}', end=' ')
