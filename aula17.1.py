valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: '))) #vai fazer digitar 5 valores
for c, v in enumerate(valores): #vai VARRER E ler os valores digitados acima enumerados da posicao 0 até 4
    print(f'Na posição {c} encontrei o valor {v}') #enumera os valores dando a posição a cada loop
