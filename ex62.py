print('='*40)
print('10 Primeiros termos de uma PA')
print('='*40)
a1=int(input('Digite o primeiro termo de uma PA: '))
r=int(input('Digite a razão da PA: '))
total = 0
mais = 10
cont = 1
while mais != 0:
    total = total + mais
    while cont <= total:
       print('{} '.format(a1),end='')
       a1 = a1 + r
       cont = cont + 1
    print('\nPausa')
    mais = int(input('Quantos termos a mais você quer mostrar? '))
print('FIM')