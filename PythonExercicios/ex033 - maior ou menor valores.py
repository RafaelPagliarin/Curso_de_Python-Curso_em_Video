# faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.

primeiro = int(input('Digite um número: '))
segundo = int(input('Digite outro número: '))
terceiro = int(input('Digite mais um número: '))

if primeiro > segundo and primeiro > terceiro:
    maior = primeiro
    if segundo > terceiro:
        menor = terceiro
    else:
        menor = segundo
else:
    if segundo > terceiro:
        maior = segundo
        if primeiro > terceiro:
            menor = terceiro
        else:
            menor = primeiro
    else:
        maior = terceiro
        if primeiro > segundo:
            menor = segundo
        else:
            menor = primeiro

print(f'O maior número digitado é {maior} e o menor é {menor}.')


