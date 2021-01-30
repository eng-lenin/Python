from random import randint
from time import sleep
computador = randint(0,5) #aqui puxei a biblioteca random e usei o módulo randint
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador=int(input('Em que número eu pensei? '))
print('LOADING...')
sleep(2) #importei esse módulo da biblioteca time
if computador==jogador:
    print('Parabéns, você leu minha mente, eu pensei no número {}'.format(computador))
else:
    print('Você perdeu, eu pensei no número {} e não no {}'.format(computador, jogador))
