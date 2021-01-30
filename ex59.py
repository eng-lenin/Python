from time import sleep
print('Bem vindo ao programa de cálculos.')
sair = False
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
while not sair:
    print('-='*20)
    comando=int(input("[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos Números\n[5] Sair\n Qual é a sua opção? "))
    if comando == 1:
        print('A soma de {} e {} é {}'.format(n1,n2,n1+n2))
    elif comando == 2:
        print('O produto de {} e {} é {}'.format(n1, n2, n1*n2))
    elif comando == 3 and n1>n2:
        print('O maior número é {}'.format(n1))
    elif comando == 3 and n1<n2:
        print('O maior número é {}'.format(n2))
    elif comando == 3 and n1==n2:
        print('Os números são iguais')
    elif comando == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif comando==5:
        print('Finalizando...')
        sair = True
    else:
        print('Opção inválida.\nTente novamente.')
    sleep(1)
print('\33[31mVolte sempre!\33[m')

