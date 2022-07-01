# desenvolva uma lógica que leia o peso e a altura de uma pessoa.
# calcule o IMC e mostre seu status, de acordo com a tabela abaixo

# abaixo de 18.5 - abaixo do peso
# entre 18.5 e 25 - peso ideal
# 25 até 30 - sobrepeso
# 30 até 40 - obesidade
# acima de 40 - obesidade mórbida

peso = float(input('Digite seu peso, em kg: '))
altura = float(input('Digite sua altura, em m: '))

imc = peso / altura**2

if imc < 18.5:
    print(f'Seu IMC é de {imc:.2f}, isso te coloca na categoria: Abaixo do peso')
elif imc <= 25:
    print(f'Seu IMC é de {imc:.2f}, isso te coloca na categoria: Peso normal')
elif imc <= 30:
    print(f'Seu IMC é de {imc:.2f}, isso te coloca na categoria: Sobrepeso')
elif imc <= 40:
    print(f'Seu IMC é de {imc:.2f}, isso te coloca na categoria: Obesidade')
else:
    print(f'Seu IMC é de {imc:.2f}, isso te coloca na categoria: Obesidade Mórbida')


