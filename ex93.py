jogador = dict()
print('-='*20)
print(f'{"Estatistica da Bola":^40}')
print('-='*20)
jogador['nome']=str(input('Nome: '))
partidas=list()
total=int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range (0, total):
    partidas.append(int(input(f'Quantos gols fez na partica {c}? ')))
jogador['gols']=partidas[:]
print('-='*20)
print(jogador)
print('-='*20)
for k, v in jogador.items():
    print(f'O campo {k} tem valor: {v}')
print('-='*20)
print(f'O jogador {jogador["nome"]} jogou {len(partidas)} partidas e fez {sum(jogador["gols"])} gols')
print()
for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i} {jogador["nome"]} fez {v} gols.')
print('-='*20)
