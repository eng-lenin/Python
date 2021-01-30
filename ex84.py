temp = []
princ = []
mai = men = 0
print('-='*30)
print('BANCO DE DADOS DE NOMES E PESOS DOS PACIENTES')
print('-='*30)
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar=str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if continuar in 'N':
        break
print('-='*30)
print(f'Ao todo você cadastrou {len(princ)} pessoas.')
print(f'O menor peso foi de: {men} kg, da(s) pessoa(s): ',end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print( )
print(f'O maior peso foi de {mai} kg, da(s) pessoa(s): ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print( )
print('-='*30)




