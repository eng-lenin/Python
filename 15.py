d=int(input('Quantos dias você ficou com o carro? '))
km=float(input('Quantos km você andou com o carro? '))
v=(60*d)+(0.15*km)
print('O valor total a pagar é de {:.2f} R$'.format(v)
      )