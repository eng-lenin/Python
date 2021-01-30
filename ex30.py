n=int(input('Digite um número: '))
n1= n % 2 #o resto de um número par dividido por 2 é zero
if n1 == 0:
    print('Você digitou o número {}, ele é par!' .format(n))
else:
    print('Você digitou o número {}, ele é ímpar!'.format(n)
          )