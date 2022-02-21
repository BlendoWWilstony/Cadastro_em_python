def leiaint(msg):
    '''
    :param msg: input que será lido para ser feita a válidação
    :return: valor por fim já válidado
    '''
    while True:
        try:
            valor = int(input(msg))
            break
        except:
            print('\033[31mErro: Digite um numero inteiro válido\033[m')
    return valor


def linha(tamanho=42):
    '''
    :param tamanho: Tamanho que a linha deve ter
    :return: Sem retorno
    '''
    tam = int(tamanho)
    print('-' * tam)

def titulo(msg):
    '''
    :param msg: Cadeia de carcteres que sera apresentada como título da msg
    :return: Sem retorno
    '''
    msg = str(msg)
    linha()
    print(msg.center(42))
    linha()

def menu(lista):
    '''
    :param lista: lista contendo as possíveis opções de interação do sistema
    :return: opção escolhida pelo usuário dentre as opções da lista
    '''
    titulo('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    linha()
    op = leiaint('Sua opção: ')
    return op

def dados(modo='a'):
    '''
    :param modo: modo de abertura do arquivo. 'a' se o arquivo nao existir, assim será criado
    :return: varável arquivo, que serve para ser aplicar métodos sobre o arquivo
    '''
    arquivo = open('cadastro.txt', modo)

    return arquivo


def ler_arquivo_de_texto():
    '''
    :param: Sem parametro
    :return: Sem parametro
    '''
    arquivo = dados('r')
    for linha in arquivo:
        print(linha)


def inserir():
    arquivo = dados('a')
    op = 'S'
    while op in 'Ss':
        arquivo.write(input('Novo Cadastro: ') + '\n')
        op = str(input('Deseja cadastrar mais? [S/N]'))
        if op in 'Nn':
            break
