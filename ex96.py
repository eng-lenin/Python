def area(larg, comp):
    a = larg * comp
    print(f'A área do terreno em m² é de {a:.2f}')


#início do programa
print('-='*20)
print('Cálculo de Terrenos')
print('-='*20)
l = float(input('Digite a largura do terreno: '))
c = float(input('Digite o comprimento do terreno: '))
area(l,c)

