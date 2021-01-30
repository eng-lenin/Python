n=int(input(('Digite um número para ver sua tabuada: ')))
print('A tabuada do {} é: '.format(n))
for c in range (1,11):
    print('{} x {} = {} '.format(n,c,n*c))