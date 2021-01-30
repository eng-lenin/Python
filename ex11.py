a=float(input('Qual a altura da sua parede em metros?'))
l=float(input('Qual a largura da sua parede em metros?'))
t=a*l/2
print('A sua parede tem uma altura de {} metros e uma largura de {} metros, '
      'resultando em uma área de {} m², que necessitará de {} litros de tinta.'.format(a,l,a*l,t)
      )