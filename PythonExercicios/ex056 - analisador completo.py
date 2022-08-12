# desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. no final do programa, mostre:
# a média de idade do grupo
# qual o nome do homem mais velho
# quantas mulheres tem menos de 21 anos.

maisvelho = 0
mulheres_menos_21 = 0
soma_idades = 0

for c in range(0, 4):
    print()
    nome = str(input(f'Digite o nome da {c+1}ª pessoa: '))
    idade = int(input(f'Digite a idade da {c+1}ª pessoa: '))
    sexo = str(input(f'Qual o sexo da {c+1}ª pessoa [F/M]: ')).strip().upper()
    soma_idades += idade
    if (sexo == 'M') and idade > maisvelho:
        nomevelho = nome
        maisvelho = idade
    if (sexo == 'F') and idade < 20:
        mulheres_menos_21 += 1

print()
print(f'A média de idade do grupo é {soma_idades / 4:.0f} anos.')
print(f'O homem mais velho se chama {nomevelho}.')
print(f'{mulheres_menos_21} mulher(es) tem menos de 20 anos.')