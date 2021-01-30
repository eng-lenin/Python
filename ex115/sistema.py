from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if arquivoexiste(arq):
    print('Arquivo encontrado com sucesso.')
else:
    print('Arquivo não encontrado.')
    criararquivo(arq)


while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerarquivo(arq)
    elif resposta == 2:
        cabeçalho('Cadastro de Pessoa')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema, até logo!')
        break
    else:
        print('\033[31mErro! Digite uma opção válida.\033[m')
    sleep(1)

