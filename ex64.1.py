s=0
n=0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    s = s + n
    n=int(input('Digite um número [999 para parar]: '))
print('A soma entre eles foi: {} '.format(s))