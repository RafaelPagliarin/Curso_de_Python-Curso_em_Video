# faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

# função adicionada posteriormente, apenas para treinamento e fixação de conceito.
def colorir(texto):
    '''função para colocar texto em verde'''
    return f'\33[1;32m{texto}\33[m'


n = int(input('Digite o número que deseja visualizar a tabuada: '))
# , end='')
print()
print(f'''A tabuada de \33[1;32m{n}\33[m é:
 01 x {colorir(n)} = {1*n} \n 02 x {colorir(n)} = {2*n}
 03 x {colorir(n)} = {3*n} \n 04 x {colorir(n)} = {4*n}
 05 x {colorir(n)} = {5*n} \n 06 x {colorir(n)} = {6*n}
 07 x {colorir(n)} = {7*n} \n 08 x {colorir(n)} = {8*n}
 09 x {colorir(n)} = {9*n} \n 10 x {colorir(n)} = {10*n}''')

