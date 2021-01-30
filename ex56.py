somaidade=0
mediaidade=0
maioridadehomem=0
nomehomemmaisvelho = ''
totmulher20 = 0
for pessoa in range (1,5):
    nome=str(input("Digite o nome da {}ª pessoa: ".format(pessoa))).strip()
    idade=int(input('Digite a idade da {}ª pessoa: '.format(pessoa)))
    sexo=str(input('Digite o sexo [M/F] da {}ª pessoa: '.format(pessoa))).strip()
    somaidade = somaidade + idade
    if pessoa==1 and sexo in 'Mm':
        maioridadehomem=idade
        nomehomemmaisvelho=nome
    if sexo in 'Mm' and idade > maioridadehomem:
            maioridadehomem=idade
            nomehomemmaisvelho=nome
    if sexo in 'Ff' and idade > 20:
        totmulher20 = totmulher20 + 1
mediaidade= somaidade / 4
print('A média da idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomehomemmaisvelho))
print('Temos {} mulher(s) com mais de 20 anos.'.format(totmulher20))