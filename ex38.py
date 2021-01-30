n1=int(input('Digite um número: '))
n2=int(input('Digite outro número: '))
if n1 > n2:
    print('O número {} é maior do que {}'.format(n1,n2))
elif n2 > n1:
    print('O número {} é maior do que {}'.format(n2,n1))
else:
    print('Você digitou {} duas vezes, portanto, são números iguais.'.format(n1)
          )