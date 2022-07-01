parte 1 -  condições simples e compostas

obs : todo metodo tem parenteses no final (o que exatamente é metodo???)

estruturas sequenciais são realizados 1 a 1 (de cima pra baixo) [bloco de comandos], de forma que não exista outra possibilidade de realização
(como um carro numa estrada reta, sem retornos ou bifurcações)

agora imagine uma viagem onde existam 2 estradas possiveis que te levem ao mesmo lugar. Ao escolher uma das estradas,
você exclui o caminho da outra. Ou seja, existe a possibilidade de escolha.


 . comando - se/senão (if/else)

if carro.esquerda():
    bloco True
else:
    bloco False


tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')
print('--FIM--')


Dentro do python é possivel fazer uma condição simplificada 

tempo = int(input('Quantos anos tem seu carro?'))
print('carro novo' if tempo <= 3 else 'carro velho')
print('--FIM--')

