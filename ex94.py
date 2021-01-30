pessoa = dict()
galera = list()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).strip()
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Tente novamente!')
    pessoa['idade'] = int(input('Idade: '))
    soma = soma + pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        continuar = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
        if continuar in 'SN':
            break
        print('Erro! Tente novamente!')#só vai ler se não der break
    if continuar in 'N':
        break
print(galera)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma/len(galera)
print(f'A soma das idades das pessoas é {soma} e a média é {média:.2f}')
print('As mulheres cadastradas foram: ')
for p in galera:
    if p['sexo'] == 'F':#cuidar pra digitar p e não pessoas, se não imprime tudo
        print(f'{p["nome"]} ', end='...')
print()
print(f'A(s) pessoas que possue(m) idade acima da média de {média} anos:')
for p in galera:
    if p['idade'] >= média:
        print(   )
        for k, v in p.items():
            print(f'- {k} = {v}; ', end='')
