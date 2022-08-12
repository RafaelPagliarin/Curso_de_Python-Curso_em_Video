'''faça um programa que leia uma frase pelo teclado e mostre:

quantas vezes aparece a letra A
em que posição ela aparece pela primeira vez
em que posição ela aparece pela última vez'''

frase = str(input('Digite uma frase: ')).lower().strip()

print(f' A letra "a" aparece {frase.count("a")} vezes ao longo da frase \n A primeira vez na posição'
      f' {frase.find("a")+1} \n E a última vez na posição {frase.rfind("a")+1}')
