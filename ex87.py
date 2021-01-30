matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = 0
maiorseglin = 0
somacolunadois = 0
for l in range (0,3):
    for c in range (0,3):
        matriz[l][c]=int(input(f'Digite o valor [{l}, {c}]: '))
print('-='*11)
for l in range (0,3):
    for c in range (0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar = somapar + matriz[l][c]
    print()
print('-='*11)
print(f'A soma dos valores pares da matriz é {somapar}')
for l in range (0,3):
    somacolunadois = somacolunadois + matriz[l][2]
print(f'A soma da coluna 2 é {somacolunadois}')
for c in range (0,3):
    if c==0:
        maiorseglin = matriz[1][c]
    else:
        if matriz[1][c] > maiorseglin:
            maiorseglin = matriz[1][c]
print(f'O maior valor da segunda linha é {maiorseglin}')