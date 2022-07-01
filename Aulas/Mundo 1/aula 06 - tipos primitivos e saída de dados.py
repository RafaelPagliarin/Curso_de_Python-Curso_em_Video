# tipos primitivos

#int (inteiros) | exemplos: 7, -4, 0, 9875
#float (reais ou flutuantes) | exemplos: 4.5 , 0.076 , -15.223 , 7.0
#bool (lógicos, ou booleanos) | exemplos: True , False (com a primeira letra maiuscula)
#str (caracteres ou strings) | exemplos: 'Olá' , '7.5' , ''


# as duas sintaxes abaixo estão corretas, a última apenas "aprimora" a primeira em alguns aspectos (mesmo que maior)
# essa sintaxe só funciona depois do python 3
print('A soma vale', s)
print('A soma vale{}'.format(s))

# Quem tiver assistindo em 2019 depois da versão 3.7 do python não precisa mais usar .format (), apenas coloque um f
# antes das aspas " " e escreva o nome da variavel dentro dos colchetes {}  exemplo: print (f'A soma de {n1} e {n2} é
# {s}')

print(f'A soma de {n1} e {n2} é {s}')