print('-='*20)
print('Bem vindo(a) ao simulador de financiamento imobiliário!')
print('-='*20)
v=float(input('Digite o valor do imóvel a ser comprado: R$ '))
s=float(input('Digite o valor do salário mensal do comprador: R$ '))
a=int(input('Digite em quantos anos será pago o imóvel: '))
print('Para comprar o imóvel de R$ {:.2f} em {} anos, a prestação mensal será de: R$ {:.2f}'.format(v,a,(v/(a*12))))
if (v/(a*12)) > (s*0.3):
    print('Seu empréstimo foi negado!')
else:
    print('Seu empréstimo foi aceito!')