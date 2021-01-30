cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
        'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um úmero entre 0 e 20: '))
    if num >= 0 and num <= 20:
        break
    print('Tente novamente.')
print(f'Você digitou o número {cont[num]}')
