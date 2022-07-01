# Dentro do pacote utilidadesCeV que criamos no desafio111, temos um módulo chamado dado. Crie uma função chamada
# leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas
# valores que sejam monetários.

from utilidadesCeV import dado, moeda

p = dado.leiadinheiro('Digite um valor: R$')
moeda.resumo(p, 35, 22)

# nesse exercicio existe um problema que não existe solução sem a proxima aula, que é tratamento de erro
# o problema consiste em digitar um valor numerico junto com letras. por ex: R$300, eu2300
