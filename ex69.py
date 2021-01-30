print('-'*30)
print('Cadastre uma Pessoa')
print('-'*30)
homens = maiores = mulheres20 = 0
while True:
    idade=int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo=str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade > 17:
        maiores = maiores + 1
    if sexo in 'Mm':
        homens = homens + 1
    if sexo in 'Ff' and idade < 20:
        mulheres20 = mulheres20 + 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if resposta not in 'Ss':
        break
print(f'Foram {maiores} pessoas maiores de idade cadastradas.')
print(f'Foram {homens} homens cadastrados.')
print(f'Foram {mulheres20} mulheres abaixo de 20 anos cadastradas.')
