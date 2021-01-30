s=str(input('Qual o seu sexo [M/F]? ')).upper().strip()[0]
while s not in 'MF':
    s=str(input('Digite novamente: '))
print('Sexo {} registrado com sucesso.'.format(s))

