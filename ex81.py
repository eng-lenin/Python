valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    sair = ' '
    while sair not in 'SN':
        sair=str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if sair in 'N':
        break
print(f'Você digitou {len(valores)} números.')
print(f'Você digitou os valores {valores}')
valores.sort(reverse=True)
print(f'Em ordem decrescente: {valores}')
if 5 in valores:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não foi encontrado.')