# crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo
# com a média atingida:

# média abaixo de 5 - reprovado
# média entre 5 e 6.9 - recuperação
# média 7 ou superior - aprovado

p1 = float(input('Digite a nota da P1: '))
p2 = float(input('Digite a nota da P2: '))
m = (p1+p2) / 2

if m >= 7:
    print(f'Média \33[32m{m}\33[m. Aluno aprovado!')
elif (m >= 5) and (m < 7):
    print(f'Média \33[33m{m}\33[m. Aluno em recuperação!')
else:
    print(f'Média \33[31m{m}\33[m. Aluno Reprovado!')
