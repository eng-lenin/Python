def leiaint(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg)).strip()
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('Erro! Digite um número inteiro.')
        if ok:
            break
    return valor



n = leiaint('Digite um número: ') #n=funcao leiint....e leiaint retorna valor, então n=valor
print(f'Você digitou o número {n}. ')