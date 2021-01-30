f=str(input('Digite uma frase: ')).strip().lower()
print('A letra "a" apareceu {} vez(es) na frase'.format(f.count('a')))
print('A letra "a" apareceu pela primeira vez na posição: {}'.format(f.find('a')+1))
print('A letra "a" apareceu pela última vez vez na posição: {}'.format(f.rfind('a')+1))

#adicionei o 1 pra não aparecer posição zero
