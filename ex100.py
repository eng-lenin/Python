from random import randint
def sorteia(lista):
    for cont in range (0, 5):
        lista.append(randint(0, 9))
    print(lista)


def somapar(lista):
    s=0
    for c in lista:
        if c % 2 == 0:
            s = s + c
    print(s)



números = list()
sorteia(números)
somapar(números)
