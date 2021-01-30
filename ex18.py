import math
a=float(input('Digite um ângulo: '))
s=math.sin(math.radians(a))
c=math.cos(math.radians(a))
t=math.tan(math.radians(a))
print('Para o ângulo de {:.3f}:\nO seno vale {:.3f}\nO cosseno vale {:.3f}\nA tangente vale {:.3f}'.format(a,s,c,t)
      )