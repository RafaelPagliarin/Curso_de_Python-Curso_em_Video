# no python vc consegue enunciar uma variável composta de 3 maneiras:
## lanche = (tupla) [lista] {dicionário}
# tupla pode ser com ou sem parenteses nos pythons mais atuais
#lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
#print(lanche[1:3])

#for cont in range(0, len(lanche)): # também funciona.
#    print(f'Eu vou comer {lanche[cont]} na posição {cont}.') #hamburguer, suco, pizza, pudim

#for comida in lanche:
#    print(f'Eu vou comer {comida}.') # aqui nesse exemplo não temos como utilizar um contador (nem sempre vc precisa)

#for pos, comida in enumerate(lanche):
#   print(f'Eu vou comer {comida} na posição {pos}.') #funciona igual o primeiro exemplo

#print('Comi pra caramba!!!')

#print(sorted(lanche)) # mostrar o lanche em ordem alfabética, ele "muda" a ordem, mas não muda de fato os locais.
# tanto que o python mostra a resposta como uma lista []

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c) # ele junta as tuplas. logo: a + b != b + a
print(c.count(5)) # conta quantas vezes o elemento 5 aparece na tupla
print(c.index(8)) # em que posição está o primeiro elemento 8?
print(c.index(5, 1)) # em que posição está o elemento 5 após a posição 1? deslocamento

# em algumas linguagens as tuplas só aceitam um tipo de dado (números, alfabético, etc). no python pode ter dados diferentes dentro da mesma tupla

# embora imutável, a tupla pode ser apagada (inteira). exemplo:
# del(lanche)

from random import randint
numal = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for n in numal:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numal)}.')
print(f'O menor valor sorteado foi {min(numal)}.')

# o python tem max/min para tuplas, não precisando criar um laço de repetição para verificar (exercicio 74)