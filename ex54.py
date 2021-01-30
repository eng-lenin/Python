from datetime import date
ano = date.today().year
count1 = 0
count2 = 0
for c in range (1,8):
    nasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    if ano - nasc < 18:
        count1 = count1 + 1
    else:
        count2 = count2 + 1
print('Ao todo tivemos {} pessoa(s) maior(es) de idade e {} pessoa(s) menor(es) de idade.'.format(count2,count1))
