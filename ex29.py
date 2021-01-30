v=float(input('A qual velocidade (km/h) está o carro? '))
if v<= 80:
    print('Abaixo do limite, obrigado! ')
else:
    print('Você está acima do limite, você deve pagar uma multa de R$ {:.2f}!' .format((v-80)*7))

