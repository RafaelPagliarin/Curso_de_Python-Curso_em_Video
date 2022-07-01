'''Cores no Terminal - aula extra (não essencial)

padrão ansi (internacional) - escape sequence

código ansi sempre começa com contrabarra \

\033[   >> sempre começa assim
sempre termina com m

\033[ "estilo da fonte;cor do texto;cor do fundo" m

exemplo: \033[0;33;44m

códigos para estilo:
0 none
1 bold (negrito)
4 underline (sublinhado)
7 negative

código para cor:
30 preto
31 vermelho
32 verde
33 amarelo
34 azul
35 magenta
36 ciano
37 cinza
97 branco

código para fundo (background)
igual ao anterior, mas com 40 (4x) e 107 para branco'''

\033[0;30;41m
\033[4;33;44m
\033[1;35;43m
\033[30:42m
\033[m (letra cinza, fundo preto. padrão do terminal)
\033[7;30m (faz uma cor de código branco e fundo preto e depois inverte para ter letra preta e fundo branco)

