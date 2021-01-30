from random import randint
from time import sleep
lista = list()
jogos = list()
cont = 0
tot = 1
quant = 0
print('-'*60)
print('{:^60}'.format(' RANDOMIZADOR DE JOGOS DA MEGA SENA '))
print('-'*60)
quant = int(input('Quantos jogos você quer sortear? '))
while tot <= quant:
    cont=0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont = cont + 1
        if cont == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot=tot+1
print('-'*60)
print('{:^60}'.format(' SORTEANDO '))
print('-'*60)
sleep(1)
for i, l in enumerate(jogos):
    print(f'Seu {i+1}º jogo sorteado foi: {l}')
    sleep(1)
print('BOA SORTE')
