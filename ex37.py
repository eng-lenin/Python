n=int(input('Digite um número inteiro para ser convertido: '))
escolha=int(input('Digite:\n1 para converter para binário\n2 para converter '
                  'para octal\n3 para converter para hexadecimal\nSua escolha é: '))
if escolha == 1:
    print('Seu número é {}, em binário ele fica: {} '.format(n,bin(n)[2:]))
elif escolha == 2:
    print('Seu número é {}, em octal ele fica: {} '.format(n,oct(n)[2:]))
elif escolha == 3:
    print('Seu número é {}, em hexadecimal ele fica: {}'.format(n,hex(n)[2:]))
else:
    print('Escolha inválida, escolha 1 para binário, 2 para octal e 3 para hexadecimal, tente novamente.')
#[2:] é pq os dois primeiros caracteres são inúteis, quero mostrar só depois disso