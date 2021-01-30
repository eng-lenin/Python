jogador = dict()
time = list()
partidas = list ()
print('-='*30)
print(f'{"Estatistica da Bola":^60}')
print('-='*30)
while True:
    jogador.clear()
    jogador['nome']=str(input('Nome: '))
    total=int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range (0, total):
        partidas.append(int(input(f'Quantos gols fez na partica {c}? ')))
    jogador['gols']=partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if continuar in 'SN':
            break
        print('Erro! Tente novamente!')
    if continuar in 'N':
        break
print('-'*70)
print('TABELA DE INFORMAÇÕES')
print('-'*70)
print(' cod  ', end='')
for i in jogador.keys():
    print(f'{i:<25}', end='')
print()
print('-'*70)
for k, v in enumerate(time):#lista
    print(f'{k:>4} ', end='')
    for d in v.values():#dicionário dentro da lista
        print(f'{str(d):<25}', end='')
    print()
print('-'*70)
while True:
    busca = int(input('Digite o cod do jogador para ver as estatísticas (999 para sair): '))
    if busca == 999:
        break
    if busca >= len(time):
        print('Digite um código válido.')
    else:
        print(f'  --- Levantamento do Jogador {time[busca]["nome"]} ---')
        for i, g in enumerate(time[busca]['gols']):
            print(f'No jogo {i} fez {g} gols.')
print('-'*70)

