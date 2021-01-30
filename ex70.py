print('-'*30)
print('LOJA SUPER BARATÃO')
print('-'*30)
contador=0
menor=0
total=0
produtomaisbarato=' '
maiscaros = 0
while True:
    produto=str(input('Qual o nome do produto? ')).strip()
    valor=float(input('Qual o valor do produto? R$ '))
    contador = contador + 1
    total = total + valor
    if valor > 1000:
        maiscaros = maiscaros + 1
    if contador == 1:
        menor = valor
        produtomaisbarato = produto
    if contador > 1 and valor < menor:#esse if poderia ser um "or" do if acima
        menor = valor
        produtomaisbarato=produto
    print('-'*30)
    sair= ' '
    while sair not in 'SN':
        sair=str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if sair == 'N':
        break
print(f'Total gasto na compra foi R$ {total:.2f}')
print(f'{maiscaros} produtos custam mais do que R$ 1000')
print(f'Produto mais barato foi: {produtomaisbarato}, custou R$ {menor:.2f}')