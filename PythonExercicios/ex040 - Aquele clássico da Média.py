# crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo
# com a média atingida:

# média abaixo de 5 - reprovado
# média entre 5 e 6.9 - recuperação
# média 7 ou superior - aprovado

p1 = float(input('Digite a nota da P1: '))
p2 = float(input('Digite a nota da P2: '))
media = (p1 + p2) / 2

if media >= 7:
    print(f'Média \33[32m{media}\33[m. Aluno aprovado!')
elif (media >= 5) and (media < 7):
    print(f'Média \33[33m{media}\33[m. Aluno em recuperação!')
else:
    print(f'Média \33[31m{media}\33[m. Aluno Reprovado!')
