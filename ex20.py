import random
n1=input('Digite o nome do primeiro aluno: ')
n2=input('Digite o nome do segundo aluno: ')
n3=input('Digite o nome do terceiro aluno: ')
n4=input('Digite o nome do quato aluno: ')
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('A ordem de apresentação é: {}'.format(lista)
      )
#atencao, nesse ecercicio não deu pra fazer como no anterior, atribuindo uma variável ao shuffle, a lista muda
# simplesmente embaralha a lista e a usa a lista lá embaixo como variável