# crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar
# se a expressão passada está com os parênteses abertos ou fechados na ordem correta.

texto = str(input('Digite uma expressão: ')).strip().lower()
pilha = []

for x in texto:
    if x == '(':
        pilha.append(x)
    elif x == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
