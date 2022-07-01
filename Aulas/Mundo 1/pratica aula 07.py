# nome = input('Qual é seu nome? ')
# print(f'Prazer em te conhecer {nome:=^20}!')

# {nome:20} - usa o nome e preenche até dar 20 espaços
# {nome:>20} - preenche antes do escrito
# {nome:<20} - preenche depois do escrito
# {nome:^20} - coloca o escrito centralizado em 20 espaços
# {nome:=^20} - coloca o escrito centralizado, cercado por = em 20 espaços

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print(f'A soma vale {(n1+n2)}, \n o produto é {n1*n2}, \n a divisão é {n1/n2:.3f}', end=' ')
print(f'Divisão inteira {n1//n2} e potência {n1**n2}')
