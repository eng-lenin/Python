from datetime import date
nas = int(input('Digite o ano em que você nasceu: '))
ano = date.today().year  # importar o ano atual
if (ano-nas) > 18:
    print('Você já deveria ter se alistado {} anos atrás!'.format(ano-nas-18))
elif (ano-nas) < 18:
    print('Você ainda não precisa se alistar, faltam {} anos!'.format(18-(ano-nas)))
else:
    print('Você tem ou completa {} anos nesse ano, já está na hora. Corra se alistar!'.format(ano-nas))
