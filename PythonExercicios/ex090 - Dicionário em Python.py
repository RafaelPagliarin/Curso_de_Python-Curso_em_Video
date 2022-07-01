# faça um programa que leia nome e média de um aluno, guardando também a situação num dicionário.
# no final, mostre o conteúdo da estrutura na tela


aluno = dict()
aluno['nome'] = str(input('Digite o nome do Aluno: '))
aluno['media'] = float(input(f'Digite a média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 7 > aluno['media'] > 5:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print('-=-' * 10)
for c, v in aluno.items():
    print(f'{c} é igual a {v}.')
print('-=-' * 10)

