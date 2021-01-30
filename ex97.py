def escreva(msg):
    tam = len(msg)
    print(f'-'*tam)
    print(f'{msg}')
    print((f'-'*tam))


#início do programa
mensagem = str(input('Digite uma mensagem: '))
escreva(mensagem)
