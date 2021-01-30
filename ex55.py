for p in range (1,6):
    peso=float(input('informe o peso da {}ª pessoa: '.format(p)))
    if p==1:
        maior=peso
        menor=peso #no primeiro laço, a pessoa de maior e menor peso é a primeira pessoa
    else:#nos outros, se o peso for maior, ela é a maior, se for menor, ela é a menor, repetindo a cada laço
        if peso > maior:
            maior = peso
        if peso < menor:
            menor=peso
print('A pessoa de maior peso tem {:.2f} kg e a de menor peso tem {:.2f} kg.'.format(maior,menor))
#um outro jeito de fazer seria dizer que o menor é zero e o maior um número gigante