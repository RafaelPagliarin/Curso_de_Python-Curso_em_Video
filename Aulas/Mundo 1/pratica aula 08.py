# quando se "puxa" toda a biblioteca, precisamos enunciar ela antes da função. Como "math.sqrt"
#import math
#num = int(input('Digite um número: '))
#print(f'A raiz de {num} é igual a {math.floor(math.sqrt(num))}')



# quando se puxa algo especifico de dentro da biblioteca, não precisa enunciar a biblioteca como no exemplo acima
#from math import sqrt, floor
#num = int(input('Digite um número: '))
#print(f'A raiz de {num} é igual a {floor(sqrt(num))}')

# podemos usar a biblioteca random para gerar numeros randoms (igual aprendi no visualg)
#random.random >>> randomiza algo entre 0 e 1
#random.randint(a,b) >>> randomiza um numero inteiro entre a e b
import random
print(random.randint(1,10))

import emoji
print(emoji.emojize('Olá, mundo :scream:', language='alias'))

# preciso arrumar a biblioteca do emoji. preciso aprender a baixar no site e instalar sem ser por aqui