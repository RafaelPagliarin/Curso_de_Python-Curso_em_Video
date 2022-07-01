# crie um programa que escreva "Olá, mundo!" na tela.

msg = str('Olá, Mundo!').strip() #coloquei strip na mensagem para eliminar possiveis erros de digitação (espaços antes/depois da mensagem)
print()
print('\33[32m-=-\33[m' * 10) # usei o código de cor verde aprendido na aula 11
print(f'{msg:^30}') # ao invés de colocar a mensagem simples, resolvi usar uma variável e editar a posição dela (centralizando)
print('\33[32m-=-\33[m' * 10)
