from random import randint
print('-='*30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*30)
while True:
    jogador=int(input('Escolha um número: '))
    computador=randint(0,10)
    total = computador + jogador
    parimpar = ' '
    while parimpar not in 'PI':#vai ficar preso aqui até digitar P ou I
        parimpar = str(input('Escolha se quer par ou ímpar [P/I]: ')).strip().upper()[0]
    if parimpar == 'P' and total % 2 == 0:
        print('Você venceu!')
        print(f'Você escolheu {jogador} e o computador {computador}, o total foi {total} que é PAR.')
    if parimpar == 'P' and total % 2 == 1:
        print('Você Perdeu!')
        print(f'Você escolheu {jogador} e o computador {computador}, o total foi {total} que é ÍMPAR.')
    if parimpar == 'I' and total % 2 == 0:
        print('Você Perdeu!')
        print(f'Você escolheu {jogador} e o computador {computador}, o total foi {total} que é PAR.')
    if parimpar == 'I' and total % 2 == 1:
        print('Você Perdeu!')
        print(f'Você escolheu {jogador} e o computador {computador}, o total foi {total} que é ÍMPAR.')
    sair=str(input('Vamos jogar novamente [S/N]? ')).strip().upper()[0]
    if sair == 'N':
        print('GAME OVER!')
        break