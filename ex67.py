while True:
    n=int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        print('Adeus')
        break
    print('-='*30)
    for c in range(1, 11):
        print(f'{n} x {c} = {c*n}')
    print('-='*30)

