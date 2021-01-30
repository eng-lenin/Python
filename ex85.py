num = [[], []]
valor = 0
for c in range(0,8):
    valor=int(input(f'Digite o {c+1}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-='*30)
num[0].sort()
num[1].sort()
print(f'Em ordem crescente, os valores pares digitados foram: {num[0]}')
print(f'Em ordem crescente, os valores ímpares digitados foram: {num[1]}')