#Peça ao usuário digitar o nome e mostre na tela "É um prazer te conhecer, nome"

nome = str(input('Digite seu nome: ')).strip() #coloquei o input como str para poder usar o .strip()
print(f'É um prazer te conhecer, \33[34m{nome}\33[m!') # adicionei cor a variável, só da para fazer por fora do {}