from random import randint
from time import sleep
computador = randint(0,10) #aqui puxei a biblioteca random e usei o módulo randint
print('-=-'*20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar.')
print('-=-'*20)
computador = randint(0,10) #aqui puxei a biblioteca random e usei o módulo randint
acertou = False
print('LOADING...')
sleep(2) #importei esse módulo da biblioteca time
while not acertou:
    jogador = int(input('Em que número eu pensei? '))
    if computador > jogador:
        print('Digite um número maior: ')
    if computador < jogador:
        print('Digite um número menor: ')
    else:
        acertou = True
print('Parabéns, você leu minha mente, eu pensei no número {}'.format(computador))