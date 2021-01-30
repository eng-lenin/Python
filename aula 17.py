listas
são mutáveis
se usa colchetes
pode ser:
valores =  [1,3,5]
valores = list(1, 3, 5)
valores = list() e depois ir adicionando com as fórmulas abaixo

lanche.append['pizza'] para adicionar item no fim
lanche.insert[0,'pizza'] para adicionar na posição desejada

del.lanche[3] para deletar item do index 3
lanche.pop[3] para deletar item do index 3 tbm pode ser usado, se não colocar o número deleta o último elemento
lanche.remove['pizza'] deleta a partir do valor e não do index (posição)
os índices se reposicionam

valores=list(range(4,11)) criar lista a partir de um range

 para organizar valores fora de ordem usar valores.sort
valores.sort(reverse=True) organiza ao contrário

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}') #enumera os valores dando a posição a cada loop


posso fazer:

valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: '))) #vai fazer digitar 5 valores
for c, v in enumerate(valores): #vai ler os valores digitados acima enumerados da posicao 0 até 4
    print(f'Na posição {c} encontrei o valor {v}') #enumera os valores dando a posição a cada loop


para listas
a = [0,1,2,3]
b=a
o b é igual ao a e se mudar b muda a, se mudar a muda b
para isso não acontecer se cria cópia
b=a[:]
agora se mudar b não muda a
