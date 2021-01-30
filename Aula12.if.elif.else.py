nome=str(input('Digite o seu nome: ')).strip()
if nome=='Gustavo':
    print('Você tem um nome lindo, {}'.format(nome))
elif nome == 'Maria' or nome == 'Pedro' or nome == 'João':
    print('Seu nome é muito popular no Brasil, {} '.format(nome))
elif nome in 'Ana Mariana Juliana Bruna':
    print('Que belo nome feminino, {} '.format(nome))
else:
    print('Seu nome é bem normal, {} '.format(nome))

# é o que chamamos de linha condicional aninhada
#if só se usa uma vez, elif infinitas vezes, else nenhuma ou uma vez