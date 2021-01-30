from math import sqrt
n=float(input("Digite o tamanho do cateto 1: " ))
m=float(input('Digite o tamanho do cateto 2: ' ))
h=sqrt(n*n+m*m)
print('Para um triângulo retângulo com um cateto valendo {} e outro cateto valendo {} a hiptenusa vale {}'.format(n,m,h)
      )
#tem uma função no math que é a hypot, faz a mesma coisa
#como importei somente a sqrt não precisei referenciar o math na linha 4