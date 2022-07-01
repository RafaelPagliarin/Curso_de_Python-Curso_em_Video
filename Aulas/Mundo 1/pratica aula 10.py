'''=== estrutura simples (sem else) ===
nome = str(input('Qual é seu nome? '))
if nome == 'Rafael':
    print('Que nome lindo você tem!')
print(f'Bom dia {nome}!')

=== estrutura composta (com else) ===
nome = str(input('Qual é seu nome? '))
if nome == 'Rafael':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia {nome}!') '''

=== programa classico de notas ===

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
print(f'A sua média foi {(n1+n2)/2:.1f}')
if ((n1+n2)/2) >= 6.0:
    print('Sua média foi boa! parabéns!')
else:
    print('Sua média foi ruim! estudo mais!')
