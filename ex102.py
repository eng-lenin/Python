def fatorial(n, show=False):
    """
    -> Retorna o fatorial de um número
    :param n: número que vai calcular o fatorial
    :param show: opcional, show=True mostra, False não mostra
    :return: o valor fatorial de um número n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c>1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        f = f*c
    return f

#Programa
n = int(input('Digite um número para ver seu fatorial: '))
print(fatorial(n, show = True))#cuidado com os parênteses, confuso
help(fatorial)#para mostrar detalhes da função