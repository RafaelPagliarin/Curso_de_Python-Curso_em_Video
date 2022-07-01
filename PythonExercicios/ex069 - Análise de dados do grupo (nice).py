# crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
# se o usuário quer ou não continuar. No final, mostre:

# a. quantas pessoas tem mais de 18 anos.
# b. quantos homens foram cadastrados.
# c. quantas mulheres tem menos de 20 anos.

tot18 = homem = mm20 = 0
while True:
    cont = ' '
    sexo = ' '
    idade = int(input('Digite a idade: '))
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [F/M]: ')).strip().upper()[0]
        if sexo not in 'MF':
            print('Opção inválida.')
    if idade > 18:
        tot18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mm20 += 1
    while cont not in 'SN':
        cont = str(input('Deseja continuar [S/N] ? ')).strip().upper()[0]
        if cont not in 'SN':
            print('Opção inválida.')
    if cont == 'N':
        break

print(f'{tot18} pessoas com mais de 18 anos foram cadastradas.')
print(f'{homem} homens foram cadastrados.')
print(f'{mm20} mulheres com menos de 20 anos foram cadastrados')