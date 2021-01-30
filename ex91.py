from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1,7),
        'jogador2': randint(1,7),
        'jogador3': randint(1,7),
        'jogador4': randint(1,7)}
print('-='*30)
print(f'{"JOGO DE DADOS":^60}')
print('-='*30)
sleep(0.5)
for k, v in jogo.items():#aqui é dicionário, ao invés do index número usa a palavra declarada
    print(f'{k} tirou {v}')
    sleep(0.5)
ranking = list()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print(f'{"RANKING":^60}')
print('-='*30)
for i, v in enumerate(ranking): #aqui é lista
    print(f'{i+1}º lugar: {v[0]} com {v[1]} pontos')
    sleep(0.5)