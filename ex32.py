from datetime import date
ano=int(input('Que ano você quer analisar? Digite 0 para o seu ano atual: '))
if ano == 0:
    ano = date.today().year #importar o ano atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:#o != quer dizer diferente
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano)
          )