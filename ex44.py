print('{:=^40}'.format(' LOJAS GUANABARA '))
preco=float(input('Peço das compras é: R$ '))
print('Formas de Pagamento: \n'
      '[1] Á vista em dinheiro ou cheque\n'
      '[2] Á vista no cartão\n'
      '[3] 2x no cartão\n'
      '[4] 3x ou mais no cartão\n')
opcao=int(input('Qual será a opção de pagamento? Digite o número correspondente: '))
if opcao == 1:
    print('O valor da compra com o desconto de 10% fica em: R$ {:.2f}'.format(preco*0.9))
elif opcao == 2:
    print('O valor da compra com o desconto de 5% fica em: R$ {:.2f}'.format(preco*0.95))
elif opcao == 3:
    print('O valor da compra não tem desconto, fica em: R$ {:.2f}'.format(preco))
elif opcao == 4:
    print('O valor da compra em 3x ou mais tem 20% de jutos e fica em: R4 {:.2f}'.format(preco*1.2))

#poderia ter criado uma outra variável chamada, por exemplo, total
#e ter dado o print só na última linha com o valor certo pra variável que fosse escolhida
#dá pra adicionar input pro número de parcelas na opcao 4 já calcular o valor total e das parcelas escolhidas
