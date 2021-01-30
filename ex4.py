a=input('Digite algo:')
print('O tipo primitivo desse valor é',type(a))
print('Só tem espaços?',a.isspace())
print('É um número?',a.isnumeric())
print('É alfabético?',a.isalpha())
print('É alfanumérico?',a.isalnum())
print('Está em letras maiúsculas?',a.isupper())
print('Está em letras minúsculas?',a.islower())
print('Está capitalizada?',a.istitle())

#se for número retorna com True, se não for retorna com false
#isalpha confere se é letra
#is alnum retorna se é alfanumérico, que é letra e número juntos
#is upper para ver se está somente com letras maiúsculas
#tem muitos