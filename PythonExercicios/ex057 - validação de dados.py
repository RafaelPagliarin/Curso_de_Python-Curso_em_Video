# faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação
# novamente até ter um valor correto.

sexo = None
while (sexo != 'F') and (sexo != 'M'):
    sexo = str(input('Qual seu sexo? [F/M] :')).upper().strip()[0] # usando fateamento e pegando só a 1ª letra
    if (sexo != 'F') and (sexo != 'M'):
        print(f'Resposta \33[31m{sexo}\33[m inválida! Por favor, responda novamente.')
    else:
        if sexo == 'F':
            print('Sexo: Feminino')
        else:
            print('Sexo: Masculino')