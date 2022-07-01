Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print('Estou aprendendo Python')
Estou aprendendo Python
print(7+4)
11
print('7+4')
7+4
print ('7'+'4')
74
# aqui vemos  a diferença entre dar print em números sem aspas, com aspas em tudo e com aspas apenas nos números (e não no operador)
# veja que o + pode juntar duas mensagens. A virgula ( , ) faz o mesmo papel, mas existem algumas diferenças entre os 2 a serem aprendidas ainda.
# juntar duas strings (com o +) se chama concatenação.

print ('Olá' + 5)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print ('Olá' + 5)
TypeError: can only concatenate str (not "int") to str
print('Olá' , 5)
Olá 5

# variáveis funcionam como: nome = 'guanabara' , onde o = corresponde a "recebe"

nome = 'Guanabara'
idade = 25
peso = 75..8
SyntaxError: invalid syntax
peso = 75.8
print(nome,idade,peso)
Guanabara 25 75.8


# e para interagir com o usuário, pedindo para que ele insira dados usamos o comando "input"
nome = input('Qual é seu nome?')
Qual é seu nome?Rafael
idade = input('Quantos anos vc tem?')
Quantos anos vc tem?30 anos
peso = input('Qual o seu peso?')
Qual o seu peso?102kg
print(nome, idade, peso)
Rafael 30 anos 102kg


# mas para criar um script dos comandos acima, clicamos em File>New File. Abrirá uma janela e escreveremos os comando lá, salvando o script em algum lugar


# abra o script e mande dar  "run", assim ele vai rodar automatico aquilo que foi colocado.

