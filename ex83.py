expr=str(input('Digite a expressão: '))
pilha = []
for simb in expr:#para cada símbolo da expressão
    if simb in '(':
        pilha.append('(')
    elif simb in ')':
        if len(pilha) > 0:
            pilha.pop()#se o comprimento da pilha for maior que zero já se adicionou ( e aí o pop vai apagar o último, como tá lendo/varrendo em ordem, quando achar o primeiro ) vai apagar o último (
        else:
            pilha.append(')')
if len(pilha) > 0:
    print('Expressão inválida, confira os parênteses.')
else:
    print('Expressão válida.')

#resumindo, toda vez que aparece um ) ele vai achar o ( adicionado anteriormente e apagar ou adicionar um ) se não houver
#se o comprimento da PILHA não for zero é pq tá errado