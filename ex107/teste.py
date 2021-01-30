import moeda
preço = float(input('Digite o preço: R$ '))
print(f'A metade do preço R$ {preço} é R$ {moeda.metade(preço):.2f}')
print(f'O dobro do preço R$ {preço} é R$ {moeda.dobro(preço)}')
print(f'Aumentndo o preço {preço} em 10% temos R$ {moeda.aumentar(preço, 10)}')