n=str(input('Digite o seu nome completo: ')).strip()
n1=n.split()
print('Seu primeiro nome é: {} '.format(n1[0]))
print('Seu último nome é: {} '.format(n1[len(n1)-1]))

#pra mostrar o último, peguei o comprimento do n1 e fiz -1 dentro dos colchetes de mostrar posição
