print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
a=float(input('Digite o primeiro lado de um triângulo: '))
b=float(input('Digite o segundo lado de um triângulo: '))
c=float(input('Digite o terceiro lado de um triângulo: '))
if a < b + c and b < a + c and c < a + b and a==b==c:
    print('O seu triângulo de lados {}, {} e {} pode ser formado e é equilátero!'.format(a,b,c))
elif a < b + c and b < a + c and c < a + b and a==b or a==c or b==c:
    print('O seu triângulo de lados {}, {} e {} pode ser formado e é isóceles!'.format(a,b,c))
elif a < b + c and b < a + c and c < a + b and a != b != c != a: #não precisaria colocar o != a porque fiz a linha elif explicando o isóceles
    print('O seu triângulo de lados {}, {} e {} pode ser formado e é escaleno!'.format(a,b,c))
else:
    print('O seu triângulo não pode ser formado com esses comprimentos.')

#poderia ser if dentro do if também vou criar o ex 42.1 para mostrar