import moeda
preço = float(input('Digite o preço: R$ '))
print(f'A metade do preço {moeda.moeda(preço)} é {moeda.moeda(moeda.metade(preço))}')
print(f'O dobro do preço {moeda.moeda(preço)} é {moeda.moeda(moeda.dobro(preço))}')
print(f'Aumentndo o preço {moeda.moeda(preço)} em 10% temos {moeda.moeda(moeda.aumentar(preço, 10))}')