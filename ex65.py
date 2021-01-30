numero = contador = soma = media = maior = menor = 0
pergunta = 's'
while pergunta in 'Ss':
    numero=int(input('Digite um número: '))
    pergunta=str(input('Você quer continuar [S/N]? ')).strip().upper()[0]
    soma = soma + numero
    contador = contador + 1
    if contador == 1:
        menor = numero
        maior = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
media = soma / contador
print('Você digitou {} números, a soma deles foi: {} e a média foi: {:.2f} '.format(contador, soma, media))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior,menor))
