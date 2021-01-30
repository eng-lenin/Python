import math
n=float(input('Digite um número: '))
inteiro=(math.floor(n))
print('O número inteiro de {} é {}'.format(n,inteiro)
      )
#poderia ter usado o trunc, ele corta só a parte inteira do número
#poderia usar o ceil e ele arredondaria para o próximo numero inteiro
#poderia ter importado somente a função
#from math import floor
#na linha 3 não precisaria do math. para chamar a função, somente digitar o floor
#nem precisaria importar o módulo, no básico tem a função int que retorna o inteiro