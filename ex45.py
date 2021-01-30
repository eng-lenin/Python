import random
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
print('{:=^40}'.format(' Vamos jogar JO KEN PO !!!! '))
j=int(input('[0] Pedra\n[1] Papel\n[2] Tesoura\nQual é a sua jogada? '))
print('-='*20)
c=random.randint(0,2)
print('Você jogou {}'.format(itens[j])) #é o item... tem posição 0, 1 e 2
print('O computador jogou {}'.format(itens[c]))
print('-='*20)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
if c == 0:
    if j == 0:
        print('Empate')
    elif j==1:
        print('Você venceu')
    elif j==2:
        print('Você perdeu')
    else:
        print('Jogada inválida, tente novamente.')
elif c == 1:
    if j == 0:
        print('Você perdeu')
    elif j== 1:
        print('Empate')
    elif j==2:
        print('Você venceu')
    else:
        print('Jogada inválida, tente novamente')
elif c==2:
    if j==0:
        print('Você venceu')
    elif j==1:
        print('Você perdeu')
    elif j==2:
        print('Empate')
    else:
        print('Jogada inválida, tente novamente')
