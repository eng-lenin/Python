n=str(input('Digite o seu nome completo: ')).strip()
print('Seu nome em letras maiúsculas é: {}'.format(n.upper()))
print('Seu nome em letras minúsculas é {}'.format(n.lower()))
print('Seu nome tem {} letras'.format(len(n)-n.count(' ')))
separa=n.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0],len(separa[0])))
#poderia ser assim também: print('Seu primeiro nome tem {} letras'.format(n.find(' ')))
#strip tira os espaços em lugares errados, começo e fim
