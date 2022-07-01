# crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços
# frase que se lida de trás pra frente é igual (desconsiderando espaços)
# apos a sopa
# a sacada da casa
# anotaram a data da maratona

frase = str(input('Digite uma frase: ')).strip()

separado = frase.split()
junto = ''.join(separado).lower()
n = len(junto)
inverso = ''

for letra in range(n-1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    print(f'A frase "{frase}" é um palindromo')
else:
    print(f'A frase "{frase}" não é um palindromo')


# existe também um "macete" do fateamento

frase = str(input('Digite uma frase: ')).strip()

separado = frase.split()
junto = ''.join(separado).lower()
n = len(junto)
inverso = junto[::-1] # a sacada está aqui!

if inverso == junto:
    print(f'A frase "{frase}" é um palindromo')
else:
    print(f'A frase "{frase}" não é um palindromo')