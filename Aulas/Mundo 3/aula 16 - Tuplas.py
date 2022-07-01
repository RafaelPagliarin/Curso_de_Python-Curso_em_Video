# uma variavel (simples), quando declarada, "é guardada" num espaço vazio na sua memória
# quando colocamos uma definição para a variável, por exemplo "lanche = 'hamburguer'" o 'hamburguer' vai ser guardado
# no espaço vazio reservado para a variável lanche.
# se vc tentar colocar outra entrada para esta variável, o valor guardado será destruido e o novo substituirá o antigo

# quando queremos mais de 1 valor para a variável no python, podemos usar as TUPLAS, variáveis compostas.

# variável simples = guarda apenas 1 valor
# variável composta = guardam vários valores.
# existem 3 tipos:
# 1. tuplas
# 2. listas
# 3. dicionários

# essa aula é sobre TUPLAS.
# para identificar items dentro das tuplas usamos indices, que começam em 0. (igual nas strings já vistas)
# lanche = (hamburguer, suco, pizza, pudim) = (0,1,2,3)

# tudo o que aprendemos sobre strings, fateamento, etc. valem aqui tbm

# print(lanche[2]) >>> pizza
# print(lanche(0:2]) >>> hamburguer, suco #lembrando que o último valor marcado nunca é considerado.
# print(lanche[1:]) >>> vai do suco[1] até o final
# print(lanche[-1] >>> pudim (o último). quando colocamos negativos ele começam do último elemento e voltam de 1 em 1


# também dá para usar o "for in" em variáveis compostas.
# for c in lanche: # o python criará uma variável c para lanche
# print(c)

# AS TUPLAS SÃO IMUTÁVEIS!
# se por acaso, vc não gosta de pudim e gostaria de trocar por sorvete. Não é possível fazer no python.
# dentro do programa rodando não da para mudar, só se vc "parar" o programa e manualmente alterar a tupla.
