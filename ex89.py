ficha = list()
while True:
    continuar = ' '
    nome = str(input('Digite o nome do aluno: ')).strip()
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota2+nota1)/2
    ficha.append([nome, [nota1, nota2], media])
    while continuar not in 'SN':
        continuar=str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if continuar in 'N':
        break
print('-='*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-='*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*26)
    opc=int(input('Deseja ver as notas de algum aluno? (999 para sair) '))
    if opc == 999:
        break
    elif opc <= len(ficha) - 1:
        print(f'As notas de {ficha[opc][0]} foram {ficha[opc][1]}')
