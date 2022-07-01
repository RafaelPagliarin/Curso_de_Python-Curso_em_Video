# crie um programa que tenha uma função chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa
# retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições

def voto(ano):
    """
    -> Função que recebe ano de nascimento, calcula idade e diz estado de voto da pessoa.
    :param ano: ano de nascimento do usuário
    :return: retorna se voto é negado, opcional ou obrigatório
    """
    from datetime import date #escopo de importação. bom para reduzir uso de memória do programa
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


# Programa Principal
n = int(input('Digite ano de nascimento: '))
print(voto(n)) #chamando a função dentro do print


