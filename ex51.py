print('='*40)
print('10 Primeiros termos de uma PA')
print('='*40)
a1=int(input('Digite o primeiro termo de uma PA: '))
r=int(input('Digite a razão da PA: '))
a10=a1+(10-1)*r
for c in range (a1, a10+r, r):
    print(c)
