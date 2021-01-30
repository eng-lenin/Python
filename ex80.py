lista = []
for c in range (0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:#se for o primeiro número ou maior do qu eo último da lista vai pro final da lista
        lista.append(n)
        print('Adicionado com sucesso no final da lista.')
    else:
        pos=0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                print(f'Adicionado na posição {pos}')
                break#ele vai adicionar no começo se for menor que o da posição zero, se não confere a 1, a 2, a 3...
            pos = pos + 1
print(f'A sua lista em ordem é: {lista}')