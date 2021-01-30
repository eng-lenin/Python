import moeda
preço = float(input('Digite o preço: R$ '))
taxa = float(input('Digite a taxa: '))
print(f'A metade do preço {moeda.moeda(preço)} é {moeda.metade(preço, True)}')
print(f'O dobro do preço {moeda.moeda(preço)} é {moeda.dobro(preço, True)}')
print(f'Aumentando o preço {moeda.moeda(preço)} em {taxa}% temos {moeda.aumentar(preço, taxa, True)}')
print(f'Diminuindo o preço {moeda.moeda(preço)} em {taxa}% temos {moeda.diminuir(preço, taxa, True)}')