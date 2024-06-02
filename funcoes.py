import os

def printar_linha():
    print()
    print("-" * 50)
    print()

def printar_opcoes(opcoesDisponiveis):
    print("Opcoes disponiveis:")
    for i in range(len(opcoesDisponiveis)):
        print(f"{i + 1} - {opcoesDisponiveis[i]}")

def escolher_opcao_index(mensagem, opcoesDisponiveis):
    opcao = input(mensagem)
    while not opcao.isnumeric() or int(opcao) < 1 or int(opcao) > len(opcoesDisponiveis):
        print("Opcao invalida.")
        opcao = input(mensagem)

    return int(opcao) - 1

def escolher_opcao(mensagem, opcoesDisponiveis):
    opcao = input(mensagem)
    while opcao not in opcoesDisponiveis:
        print("Opcao invalida.")
        opcao = input(mensagem)

    return opcao

def printar_cabecalho(mensagem):
    print("-" * 50)
    print(mensagem)
    print("-" * 50)

def limpar_terminal():
    if os.name == 'nt': # Windows
        os.system('cls')
    else: # Unix
        os.system('clear')