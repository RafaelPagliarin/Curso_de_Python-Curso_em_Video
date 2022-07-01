# aula 9 - Manipulando Cadeias de Texto

# cadeia de caracteres são frases (ou textos), porém as linguagens de programação chamam isso de cadeira de caracteres
# também chamado string (em aspas ou aspas duplas)

frase = 'Curso em Video Python'

# o python grava a string na memoria e cada caractere (incluindo o espaço) ocupa um "bloco", chamado indice.
# logo "curso em video python" ocupa 21 blocos (os indices começam em 0. logo aqui vai de 0 até 20)
# ao tratar as strings dessa maneira, podemos realizar algumas operações.

# FATIAMENTO - pegar pedaços da string
# os colchetes [] são usadas para representar listas

# frase[9] -> pega a 10º caractere da frase, no caso é o 'V'
# frase[9:13] -> pega do indice 9 até o 13 (excluindo o 13)
# frase[9:21] -> pega do indice 9 até o 21, mesmo não tendo o 21º pois vai até "o final do 20"
# frase[9:21:2] -> começa no 9, termina no 20, saltando de 2 em 2
# frase[:5] -> como não há nada antes do : ele começa do indice zero. e vai até o indice 5 (pegando até o 4)
# frase[15:] -> indica o inicio e não sabe o final, logo pega tudo do inicio até o final (caso não saiba o caractere final)
# frase[9::3] -> começa no 9, como não há número entre os 2 ':' vai até o final e vai saltar 3 (como se fosse frase[9:nada:3])


# ANÁLISE -

len(frase) -> vem de length(comprimento) - qual o comprimento da frase? 21 caracteres
frase.count('o') -> contar quantas vezes a letra o(minusculo) aparece. no caso da frase exemplo são 3 vezes
frase.count('o',0,13) -> faz a contagem já com o fatiamento. no caso da frase exemplo é apenas 1
frase.find('deo') -> vai dizer quantas vezes encontrou o termo "deo", vai mostrar em que momento começa a sequencia pedida.
frase.find('Android') -> se vc procurar algo que não existe na string, ele te retorna o valor (-1)
'Curso' in frase -> True or False (se existe o termo entre '' na frase)

# TRANSFORMAÇÃO

frase.replace('Python','Android') -> onde houver Python, substituir por Android
frase.upper() -> coloca tudo em CAPS
frase.lower() -> coloca tudo em minusculo
frase.capitalize() -> joga tudo para minusculo e só o primeiro caractere é colocado em CAPS
frase.title() -> vai analisar quantas palavras existem na string (baseado nos espaços vazios) e coloca a primeira letra de todas as palavras em CAPS
frase.strip() -> remove espaços vazios inuteis no começou e/ou final da string
#muito comum as pessoas digitarem errado e colocarem espaços a mais no começou ou no final, logo inventaram isso para facilitar
frase.rstrip() -> remove só espaços vazios à direita da string (no final)
frase.lstrip() -> remove só espaços vazios à esquerda da string (no começo)

# DIVISÃO

frase.split() -> divide a string em outras strings menores usando os espaços vazios para a divisão (cria uma lista, cada palavra vira uma string com indices individuais)
antes: [Curso em Video Python] --> depois: [[Curso] [em] [Video] [Python]]
 ('SPLIT POSSUI VÁRIAS FUNCIONALIDADES, ESTUDAR MAIS AFUNDO A FUNÇÃO. RECOMENDAÇÃO DO GUANABARA')

# JUNÇÃO

'-'.join(frase) -> jai juntar todos os elementos de "frase" usando como separador -
antes estava separado (pelo exemplo de divisão) : [[Curso] [em] [Video] [Python]]
depois do join: [Curso-em-Video-Python]