n1=int(input('Digite um número: '))
d=n1*2
t=n1*3
r=n1**(1/2)
print('O dobro de {} vale {}\nO triplo de {} vale {}\nA raiz quadrada de {} vale {:.3f}'.format(n1,d,n1,t,n1,r)
      )

#:;3f nas chaves da raiz é para limitar a 3 casas decimais flutuantes
#potência pode ser feita pela função pow também