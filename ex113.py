def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(('Erro, tente digitar um número INTEIRO novamente.'))
            continue
        except (KeyboardInterrupt):
            print('O usuário não quis digitar e parou o programa.')#na resolução ele colocou um continue e tbm um return 0, não deu certo aqui
            return 0
        else:
            return n



def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(('Erro, tente digitar um número REAL novamente.'))
            continue
        except (KeyboardInterrupt):
            print('O usuário não quis digitar e parou o programa.')#na resolução ele colocou um continue e tbm um return 0, não deu certo aqui
            return 0
        else:
            return n



n1 = leiaint('Digite um número inteiro: ')
n2 = leiafloat('Digite um número real: ')
print(f'Você digitou o número inteiro {n1}')
print(f'Você digitou o número real {n2}')
