soma=0
while True:
        n=int(input('Digite um número [999 to stop]: '))
        if n == 999:
            break
        soma = soma + n
print(f'A soma dos númeoros digitados é: {soma}')