n=int(input('Digite um número e saiba se ele é primo: '))
contador = 0
for c in range (1,n+1):
    if n % c == 0:
        contador = contador + 1
        print('\033[34m',end='') #vai escrever isso e mudar pra essa cor o print de baixo
    else:
        print('\033[33m', end='') #vai escrever isso e mudar pra essa cor o print de baixo
    print('{}'.format(c), end=' ')
if contador == 2:
    print('\n\033[mO número {} é primo'.format(n))
else:
    print('\n\033[mO número não {} é primo'.format(n))
print('\033[mO número {} foi divisível {} vez(es)'.format(n,contador))

#muito bom, revisar