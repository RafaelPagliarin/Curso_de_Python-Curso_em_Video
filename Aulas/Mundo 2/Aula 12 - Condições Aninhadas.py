aula 12 - condições aninhadas

na condição do if/else só existem duas opções. ou o argumento é True, ou False. Mas o que fazemos quando existem
 mais de 2 opções (exemplo dado em aula: imagine uma estrada que existam 3 ou mais caminhos, ao invés de 2 apenas)

então temos if/else dentro de if/else (como já vi no visualg/algoritmo)

if carro.esquerda():
    bloco 1
elif carro.direita(): ----> elif == else if
    bloco 2
elif carro.ré():
    bloco 3
else:
    bloco final

vc pode ter quantos elif forem necessários, mas sempre tem que ter um if primeiro

já o else, como sempre, é opcional