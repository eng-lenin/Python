from time import sleep
def maior(* num):
    cont = maior = 0
    print('-='*20)
    print('Analisando os valores passados...', end='')
    print()
    for valor in num:
        print(f'{valor} ' , end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont = cont + 1
    print(f'\nForam informado {cont} valores.')
    print(f'O maior valor é {maior}.')


#começo do programa
maior(2, 3, 4, 9, 1)
maior(3, 4, 5, 7, 1, 0)
