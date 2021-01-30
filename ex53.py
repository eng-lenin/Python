frase = str(input('Digite uma frase: ')).strip().upper()
separado = frase.split()
junto = ''.join(separado)
inverso = ''
for c in range (len(junto) -1 , -1 , -1):#o len -1 pq lenin tem 5 letras mas ali começa no 4, pq o 0 é o primeiro
    inverso = inverso + junto[c]#vai uma letra de cada vez, o c vai variando e somando cada letra do junto ao inverso
if junto == inverso:
    print('Sua frase é um palíndromo, pois {} é igual a {} ao contrário.'.format(junto,inverso))
else:
    print('Sua frase não é um palíndromo, pois {} é igual a {} ao contrário'.format(junto,inverso))
#o inverso poderia ter sido feito por fatiamento, eliminando a necessidade do for
#inverso = junto[::-1]