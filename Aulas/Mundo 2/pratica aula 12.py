# ================================================
# 1. Condição Simples

#nome = str(input('Qual é seu nome? '))
#if nome == 'Rafael':
#    print('Que nome bonito!')
#print(f'Tenha um bom dia, {nome}')

# =================================================
# 2. Condição Composta

#nome = str(input('Qual é seu nome? '))
#if nome == 'Rafael':
#    print('Que nome bonito!')
#else:
#    print('Seu nome é bem normal.')
#print(f'Tenha um bom dia, {nome}')

# =================================================
# 3. Condição Aninhada

nome = str(input('Qual é seu nome? '))
print()
if nome == 'Rafael':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome}')