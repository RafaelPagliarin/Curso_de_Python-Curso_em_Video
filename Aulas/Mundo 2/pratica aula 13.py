#print('Oi')
#print('Oi')
#print('Oi')
#print('Oi')
#print('Oi')
#print('Oi')


'''for c in range(0, 6):
    print(c)
print('Fim')
print()
for c in range(6, 0, -1):
    print(c)
print('Fim')
print()
for c in range(0, 7, 2):
    print(c)


n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('Fim')
# ========================================
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim...')'''

# =========================================

s = 0
for c in range(0, 4):
    n = int(input(f'Digite o {c+1}º valor: '))
    s = s + n # no python vc pode colocar "s += n"
print(f'O somatório de todos os valores foi {s}')