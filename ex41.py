n=int(input('Digite a sua idade para ver sua categoria: '))
if n>25:
    print('Você é da categoria Master')
elif 25 >= n > 19:
    print('Você é da categoria Sênior')
elif 19 >= n > 14:
    print('Você é da categoria Junior')
elif 14 >= n > 9:
    print('Você é da categoria Infamtil')
elif n<= 9:
    print('Você é da categoria Mirim')

