print('-='*30)
print('Sequência de Fibonacci')
print('-='*30)
n=int(input('Quantos números da sequência você quer que eu calcule? '))
print('~'*30)
t1 = 0
t2 = 1
cont = 3
print('{} {}'.format(t1, t2), end='')
while cont <= n:
    t3 = t1 + t2
    print(' {}'.format(t3), end='') #ele vai imprimindo o t3 novo a cada iteracao, até que o cont supere n
    t1 = t2
    t2 = t3
    cont = cont + 1
print(' FIM')
