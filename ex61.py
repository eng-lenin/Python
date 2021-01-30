print('='*40)
print('10 Primeiros termos de uma PA')
print('='*40)
a1=int(input('Digite o primeiro termo de uma PA: '))
r=int(input('Digite a razão da PA: '))
a10=a1+(10-1)*r
while a1 != a10+r:
   print('{} '.format(a1),end='')
   a1 = a1 + r