# crie um programa que tenha uma tupla com várias palavras(sem acentos). Depois disso, vc deve mostrar, para cada palavra,
# quais são as suas vogais.

lista = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
         'mercado', 'programador', 'futuro')

for palavra in lista:
    print(f'\nNa palavra \33[32m{palavra}\33[m temos: ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')
