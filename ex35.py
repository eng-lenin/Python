print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
a=float(input('Digite o primeiro lado de um triângulo: '))
b=float(input('Digite o segundo lado de um triângulo: '))
c=float(input('Digite o terceiro lado de um triângulo: '))
if a < b + c and b < a + c and c < a + b:
    print('O seu triângulo de lados {}, {} e {} pode ser formado!'.format(a,b,c))
else:
    print('O seu triângulo não pode ser formado com esses comprimentos.')
