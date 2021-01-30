d=int(input("Digite quantos km você vai percorrer e saiba o preço da sua passagem: "))
if d<= 200:
    print('Sua passagem custará {:.2f} R$ '.format(d*0.50))
else:
    print('Sua passagem custará {:.2f} R$ '.format(d*0.45))
print('A lenin airlines agradece a preferência! '
      )
