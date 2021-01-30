def voto(ano):
    from datetime import datetime#deixar somente aqui no local e não no global economiza memória
    atual = datetime.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos ainda não vota.'
    elif 18 > idade >= 16 or idade > 65:
        return f'Com {idade} anos o voto é opcional.'
    else:
        return f'Com {idade} anos o voto é obrigatório.'


print('-='*20)
print('Você já pode votar?')
print('-='*20)
ano = int(input('Digite o ano em que nasceu: '))
print(voto(ano))