pessoas = {'nome': 'Lenon', 'idade': 28, 'sexo':'M'} #ou pessoas = dict()
pessoas['nome'] = 'Lenin'
print(pessoas['nome'])
print(f'A pessoa {pessoas["nome"]} tem {pessoas["idade"]} anos')
print()
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print()
for k in pessoas.keys():
    print(k)
print()
for k in pessoas.values():
    print(k)
print()
for i, v in pessoas.items():
    print(f'{i} = {v}')

#para deletar um item: del pessoas['sexo']
#para adicionar não usa append, usa: pessoas['nome'] = str(input(.....
#o fatiamento no dicionário não é [:] e sim nome.copy()