def leiadinheiro(msg):
    ok = False
    while not ok:
        valor = str(input(msg)).replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print(f'\033[0;31mERRO! \"{valor}\" é um preço inválido!\033[m')
        else:
            ok = True
            return float(valor)
