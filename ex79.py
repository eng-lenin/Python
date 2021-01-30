listanum = list()
while True:
    n=int(input('Digite um valor: '))
    if n not in listanum:
        listanum.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado, não vou adicionar.')
    sair= ' '
    while sair not in 'NS':
        sair = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if sair in 'N':
        break
print(f'Você digitou os valores: {listanum}')