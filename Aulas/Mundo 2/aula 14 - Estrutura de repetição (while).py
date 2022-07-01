a estrutura for (vista na aula passada) não funciona em TODAS as situações. ela precisa de um limite (onde começa, onde termina)

para estruturas sem um numero especifico, podemos usar o "enquanto"
enquanto algo acontecer, faça tal coisa
enquanto algo não acontecer, faça tal coisa

enquanto não maçã
    passo
pega

while not maçã:
    passo
pega

o while tbm é melhor quando as repetições são "truncadas" e não lineares (exemplo do anda, pula, pega maçâ e pega moeda)

while not apple:
    if floor:
        passo
    elif empty:
        pula
    elif moeda:
        pega
pega macã

============================================
'''
for c in range(1,10):
    print(c)
print('Fim') '''

c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')
============================================
for c in range (1,5):
    n = int(input('Digite um valor: '))
print('Fim')

mas e se eu quiser fazer o de cima até o usuário quiser parar? não tem como usar o for
no exemplo abaixo mostra o programa fazendo a repetição até o usuário digitar zero (0)

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares.')
print('Fim')

# o exemplo acima pode parecer uma "gambiarra", preste atenção... a proxima aula mostra como
# resolver isso de forma mais "bonita"

