def aumentar(preço=0, taxa=0, formato=False):
    """
    -> aumenta o preço em tantos por cento
    :param preço: preço
    :param taxa: porcentage que quer aumentar
    :param formato: colocar true para formatar
    :return: preço aumentado da taxa
    """
    res = preço + (preço*taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    """
    -> diminui um preço em tantos por cento
    :param preço: preço
    :param taxa: porcentagem que quer diminuir
    :param formato: colocar True para formatar
    :return: preço diminuido da taxa
    """
    res = preço - (preço*taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    """
    -> dobra um valor
    :param preço: preço
    :param formato: colocar True para formatar
    :return: dobro
    """
    res = preço*2
    return res if formato is False else moeda(res)


def metade(preço=0, formato=False):
    """
    -> retorna a metade do preço
    :param preço: preço
    :param formato: se quer formatar colocar , True
    :return: metade do preço
    """
    res = preço/2
    return res if not formato else moeda(res)


def moeda(preço=0, moeda = 'R$ '):#pode colocar US$ por exemplo
    """
    -> retorna a formatação
    :param preço: preço
    :param moeda: R$ se quiser mudar usar , nova moeda
    :return: moeda formatada trocando . para , e com o símboloda moeda, por padrão R$
    """
    return f'{moeda}{preço:.2f}'.replace('.',',')

def resumo(preço=0, taxa=5):
    print('-'*60)
    print('Análise de Preço'.center(60))
    print('-'*60)
    print(f'A metade do preço {moeda(preço)} é: \t\t\t\t\t{metade(preço, True)}')#tabulação
    print(f'O dobro do preço {moeda(preço)} é: \t\t\t\t\t{dobro(preço, True)}')
    print(f'Aumentando o preço {moeda(preço)} em {taxa}% temos: \t{aumentar(preço, taxa, True)}')
    print(f'Diminuindo o preço {moeda(preço)} em {taxa}% temos: \t{diminuir(preço, taxa, True)}')