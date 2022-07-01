# Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular e mostre a área
# do terreno.

# Funções
def area(a, b):
    c = a * b
    print(f'A area do terreno é {c} m²')


# Programa Principal
print('-' * 30)
print(f'{"     Controle de Terrenos"}')
print('-' * 30)
largura = float(input('LARGURA (m): '))
altura = float(input('COMPRIMENTO (m): '))
area(largura, altura)

