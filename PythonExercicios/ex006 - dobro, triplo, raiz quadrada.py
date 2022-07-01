# crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n = int(input('Digite um número: '))
print(f'O dobro de {n} é {2*n}, seu triplo é {3*n} e sua raiz quadrada é {n**(1/2):.2}')

# aqui podemos fazer a raiz quadrada também importando sqrt da biblioteca math:
# from math import sqrt
# ... e sua raiz quadrada é {sqrt(n)}')