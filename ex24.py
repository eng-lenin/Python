c=str(input('Digite a cidade em que você nasceu: '))
c2=c.strip()
c3=c2.lower()
print(c3[:5]=='santo')

#os dois iguais são para printar ou mostrar se em c3 o caractere de zero até cinco (excluindo o cinco) é igual a santo
# o is funciona de forma similar
#o operador is deve ser usado sempre e somente quando queremos comparar a identidade de
# um objeto, isto é, seu endereço na memória.
#O ==, por sua vez, deve ser usado quando quisermos comparar valores
# (ou, na verdade, qualquer outra coisa!) de objetos.