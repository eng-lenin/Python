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


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt, tam=42):
    print(linha())
    print(txt.center(tam))
    print(linha())


def menu(lista):
    cabeçalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c+=1
    print(linha())
    opc = leiaint('Sua opção: ')
    return opc


