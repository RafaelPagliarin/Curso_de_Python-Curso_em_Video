# desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo

sega = float(input('Digite o comprimento do 1º segmento de reta: '))
segb = float(input('Digite o comprimento do 2º segmento de reta: '))
segc = float(input('Digite o comprimento do 3º segmento de reta: '))

if sega > (segb + segc) or segb > (segc + sega) or segc > (sega + segb):
    print(f'Os segmentos de reta ({sega}, {segb}, {segc}) não podem formar um triângulo.')
else:
    print(f'Os segmentos de reta ({sega}, {segb}, {segc}) podem formar um triângulo')
