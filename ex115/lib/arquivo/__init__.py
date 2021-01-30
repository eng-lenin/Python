from ex115.lib.interface import *

def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')#rt é leitura de arquivo texto
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')#wt+ é gravaçao de arquivo texto com o + indicando que cria caso não ache
        a.close()
    except:
        print('Houve algum erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt', encoding='utf-8')#esse enconding é pra conseguir ler o cento, como no nome do José que ficava Jos@
    except:
        print('Erro ao ler o arquivo.')
    else:
        cabeçalho('Pessoas Cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at', encoding='utf-8')#append text, adicionar texto
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('Houve um erro ao escrever os dados')
        else:
            print('Novo cadastro realizado com sucesso.')
            a.close()