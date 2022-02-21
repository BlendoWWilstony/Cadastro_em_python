# System for register users

from funcoes115 import *
from time import sleep

dados()

while True:
    resposta = menu(['Ver pessoas cadastrada', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        titulo('Ver pessoas cadastrada')
        ler_arquivo_de_texto()
    elif resposta == 2:
        titulo('Cadastrar nova Pessoa')
        inserir()
    elif resposta == 3:
        titulo('Saindo do sistema...')
        break
    else:
        print('ERRO: Digite um valor válido!')
    sleep(2)
    