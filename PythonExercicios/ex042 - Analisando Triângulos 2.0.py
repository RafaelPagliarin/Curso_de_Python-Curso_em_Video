# refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado

# equilátero - todos os lados iguais
# isósceles - 2 lados iguais
# escaleno - todos lados diferentes

print()
a = float(input('Digite o tamanho do 1º segmento de reta: '))
b = float(input('Digite o tamanho do 2º segmento de reta: '))
c = float(input('Digite o tamanho do 3º segmento de reta: '))
print()

if (a > (b + c)) or (b > (c + a)) or (c > (a + b)):
    print(f'Os três segmentos de reta \33[31mnão podem\33[m formar um triângulo.')
elif (a != b) and (b != c) and (a != c):
    print(f'Os três segmentos de reta \33[32mpodem\33[m formar um triângulo do tipo escaleno.')
elif (a == b) and (a == c):
    print(f'Os três segmentos de reta \33[32mpodem\33[m formar um triângulo do tipo equilátero.')
else:
    print(f'Os três segmentos de reta \33[32mpodem\33[m formar um triângulo do tipo isósceles.')

