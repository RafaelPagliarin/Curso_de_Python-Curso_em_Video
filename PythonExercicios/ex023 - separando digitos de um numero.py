'''faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados

ex: digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1
'''
from random import randint
num = int(input('Digite um número entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'O número sorteado foi: {num}')
print(f' unidade: {u} \n dezena: {d} \n centena: {c} \n milhar: {m}')

#esse exercicio possui um "problema", quando se coloca um número menor que 1000 ( ou seja, com 3 digitos ou menos)
#ele "trava", pois não consegue encontrar pelo menos 1 das casas. Para resolver precisamos usar as repetições, mas como
#ainda não aprendemos, ele ensinará o modo matématico para contornar a situação