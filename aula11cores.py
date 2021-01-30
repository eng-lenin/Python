#o ANSI padroniza alguns usos, sempre que quiser representar uma
# cor no python começar com \033[ e fechar com m após o código da cor
# \033[style ; text; background m  -> estilo, cor do texto, cor do fundo
# styles melhores são: 0, 1, 4 e 7, que são: nenhum, negrito, sublinhado e negativo (inverte as cores do texto e fundo excolhidas)
#cores que ´pe o text vai do 30 ao 37
#cores do back vão de 40 ao 47
print('\033[1;31;43m Olá mundo!!!\033[m') # o segundo código é pra encessar ali, se não vai até o fim da linha o contorno
a=2
b=3
print('Os valores são \033[34m{}\033[m e \033[31m{}\033[m'.format(a,b))

nome=str(input('Olá, qual é o seu nome? '))
print('Muito prazer em te conhecer {}{}{}'.format('\33[4;35m', nome,'\33[m'))