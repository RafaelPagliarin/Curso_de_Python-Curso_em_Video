#Peça ao usuário digitar o nome e mostre na tela "É um prazer te conhecer, nome"

nome = str(input('Digite seu nome: ')).strip() #coloquei o input como str para poder usar o .strip()
print(f'É um prazer te conhecer, {nome}!')