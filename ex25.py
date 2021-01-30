n=str(input('Qual é o seu nome? '))
n1=n.strip()
n2=n1.upper()
print('Seu nome tem a palavra SILVA: {}'.format('SILVA' in n2))
# operador novo, in mostra se tem SILVA dentro n2