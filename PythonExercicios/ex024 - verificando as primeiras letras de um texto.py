'''crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "santo" '''

city = str(input('Digite o nome de uma cidade: ')).strip()
print(f'A cidade possui "santo" no nome: {city[:5].upper() == "SANTO"}')
