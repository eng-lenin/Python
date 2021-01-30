pares = []
impares = []
while True:
    n=int(input('Digite um valor: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    sair = ' '
    while sair not in 'SN':
        sair=str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if sair in 'N':
        break
print(f'Seus valores digitados foram: {pares + impares}')
print(f'Os valores pares foram: {pares}')
print(f'Os valores ímpares foram: {impares}')