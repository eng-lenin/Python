n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
media=(n1+n2)/2
print('A média do aluno foi: {:.2f}'.format(media))
if media < 5:
    print('O aluno está Reprovado')
elif media >= 5 and media <= 6.9: #poderia escrever if 6.9 >= media >= 5:
    print('O aluno está em Recuperação')
elif media >= 7:
    print('O aluno está Aprovado!')