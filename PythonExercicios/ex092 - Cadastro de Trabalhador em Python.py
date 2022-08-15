# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) num dicionário
# se for acaso a CTPS for diferente de zero, o dicionário também receberá o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar


from datetime import date

ficha = dict()
ficha['nome'] = str(input('Digite o nome: '))
anonasc = int(input('Digite o ano de nascimento: '))
ficha['idade'] = date.today().year - anonasc
ficha['CTPS'] = int(input('Digite o número da carteira de trabalho (0 não tem): '))
if ficha['CTPS'] != 0:
    ficha['contrato'] = int(input('Digite o ano de contratação: '))
    ficha['salário'] = float(input('Digite o salário: R$'))
    ficha['aposentadoria'] = ficha['idade'] + ((ficha['contrato'] + 35) - date.today().year)
print('-=' * 16)
for k, v in ficha.items():
    print(f'  - {k:15} : {v}')
