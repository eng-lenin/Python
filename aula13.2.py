i=int(input('Início: '))
f=int(input('Fim: '))
p=int(input('Passo: '))
for c in range(i, f+1, p):#o +1 é pq sempre ignora o último
    print(c)