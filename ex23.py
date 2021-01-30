num=int(input('Digite um número quaquer de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('A unidade do número é {}, a dezena é {}, a centena é {}, o milhar é {}.'.format(u,d,c,m))

#como não sabemos condicionais vamos ter que usar a divisão exata e o resto dessa divisão exata divide novmente por 10
#assim vai mostrar cada dezena
#tentei fazer com split transformando em string, mas se digita número menor que mil dá erro, por não ter 4 casas