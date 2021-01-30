def ficha(nome='<desconhecido>', gol=0):
    print(f'O jogador {nome} fez {gol} gols. ')

#Programa Principal
n = str(input('Digite o nome do jogador: '))
g = str(input('Digite o número de gols dele: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n,g)
