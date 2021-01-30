soma = 0
contador = 0
for c in range(3,501):
    if c % 3 == 0 and c % 2 == 1:
        print(c)#todos os números ímpares múltiplos de 3 até 500
        contador = contador + 1 #somou esse 1 em todas a iteração, 83 vezes
        soma = soma + c #somou o c ao soma em todas as iterações
print('A soma de todos os números é {}'.format(soma))
print('Foram {} números encontrados entre 0 e 500 que são múltiplos de 3 e ímpares.'.format(contador))