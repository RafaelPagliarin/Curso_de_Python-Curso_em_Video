# faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

n = int(input('Digite o número da tabuada que deseja ver: '))
# , end='')
print()
print(f'''A tabuada de \33[1;32m{n}\33[m é:
 01 x \33[1;32m{n}\33[m = {1*n} \n 02 x \33[1;32m{n}\33[m = {2*n}
 03 x \33[1;32m{n}\33[m = {3*n} \n 04 x \33[1;32m{n}\33[m = {4*n}
 05 x \33[1;32m{n}\33[m = {5*n} \n 06 x \33[1;32m{n}\33[m = {6*n}
 07 x \33[1;32m{n}\33[m = {7*n} \n 08 x \33[1;32m{n}\33[m = {8*n}
 09 x \33[1;32m{n}\33[m = {9*n} \n 10 x \33[1;32m{n}\33[m = {10*n}''')

