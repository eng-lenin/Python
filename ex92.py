from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Nº da carteira de trabalho (0 de não tiver): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano da contratação: '))
    dados['Salário R$'] = float(input('Salário: R$ '))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratação'] + 35) - datetime.now().year)
for k, v in dados.items():
    print(f'- {k} = {v}')