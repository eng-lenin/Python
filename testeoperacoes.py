#ordem de precedencia () parênteses
# ** que é a potencia
# * mltiplicação / divisão // divisão inteira % resto

n1=int(input('Digite um número:'))
n2=int(input('Digite outro número:'))
soma=n1+n2
subt=n1-n2
multip=n1*n2
div=n1/n2
di=n1//n2
resto=n1%n2
pot=n1**n2
print('O resultado da soma é {},\n da subtração é {}, do produto é {}, da divisão é {:.3f}'.format(soma,subt,multip,div),end=' já o')
print(' resultado da divisão inteira é {}, do resto é {}, da potência é {}'.format(di,resto,pot)
      )
#:.3f na divisão é pra ter 3 casas decimais flutuantes
#end='' é pra no resultado ficar os dois prints na mesma linha, para uma quebra de linha seria \n