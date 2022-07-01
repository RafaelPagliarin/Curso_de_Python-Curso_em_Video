# funções são mais úteis para códigos maiores, onde existem muitas repetições

'''a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f' A soma A + B vale {s}')


# Programa Principal
soma(b=4, a=5) #se vc quiser, pode colocar a definição "forçada" das variáveis. se for explicitar, tem que ser todas.
soma(8, 9)
soma(2, 1)'''
# se vc tentar passar apenas 1 parametro aqui, vai dar erro. por exemplo: soma(4)

#============================ empacotando parametros (usando tuplas) ==================================================
# é algo que o python faz, mas várias linguagens de programação não faz. o python cria uma tupla com os n valores que vc quiser
# útil quando vc não tem um valor constante de passagem

def contador(*núm):
    print(núm)


contador(5, 7, 3, 1, 4)
contador(8, 4, 7)
contador(8, 0)

# ================================= USANDO LISTAS NAS FUNÇÕES COM PARAMETROS =========================================


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)


# o python faz passagem de parametro por referencia, diferente de outras linguagens que faz passagem por valor

