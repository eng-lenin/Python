from time import sleep
def contador(i, f, p):
    if p < 0:
        p = p * -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.3)
            cont = cont + p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont = cont - p
        print('FIM')
#se o sleep não der certo usar após o end='' um , flush=True



#Programa Principal
contador(10, 100, 10)
print('Agora é sua vez...')
ini=int(input('Digite o início: '))
fin=int(input('Digite o final: '))
pas=int(input('Digite o passo: '))
contador(ini, fin, pas)
