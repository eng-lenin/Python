s = float(input('Qual o salário do funcionário? R$ '))
if s > 1250.0:
    print('O salário corrigido do funcionário é: R$ {:.2f}'.format(s*1.10))
else:
    print('O salário corrigido do funcionário é: R$ {:.2f}'.format(s*1.15))
