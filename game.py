import random
import time
from funcoes import *


BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
UNDERLINE = '\033[4m'
RESET = '\033[0m'

CORES = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]

def exibir_com_cor(text, color):
    print(color + text + RESET)

def mostrar_corrida(pilotos, cores, positions, destino, maior_nome):
    limpar_terminal() # Limpa o console
    for index in range(len(pilotos)):
        carro = pilotos[index]
        posicao = positions[index]
        cor = cores[index]
        nomeDoCarro = carro + " " * (maior_nome - len(carro) + 3) # Usado para alinhar as pistas
        pista = "-" * posicao + f"🚘" + "-" * (destino - posicao) + "🏁"
        exibir_com_cor(f"{nomeDoCarro}: {pista}" , cor)
    print("\n")


def iniciar_corrida(pilotos, velocidade = 1):
    destino = 100
    posicoes = []
    cores = []

    maior_nome = 0
    cor_anterior = ""
    for piloto in pilotos:
        posicoes.append(0)
        cor = random.choice(CORES)
        # Evitar que dois carros tenham a mesma cor seguida
        while cor == cor_anterior: 
            cor = random.choice(CORES)
        cores.append(cor)
        cor_anterior = cor

        if len(piloto) > maior_nome:
            maior_nome = len(piloto)

    for i in range(5, 0, -1):
        print(f"A corrida começará em {i} segundos...")
        time.sleep(1)

    ordem_de_chegada = []
    while len(ordem_de_chegada) < len(pilotos):
        for piloto_idx in range(len(pilotos)):
            piloto = pilotos[piloto_idx]
            if piloto not in ordem_de_chegada: # Só incrementa a posicao para os pilotos que ainda nao chegaram na final
                posicoes[piloto_idx] += random.randint(1, 3) # Incrementa a posicao do carro de forma aleatoria
                if posicoes[piloto_idx] >= destino: # Checa se o carro chegou ao final
                    posicoes[piloto_idx] = destino # Ajusta a posição para o final, caso tenha passado
                    ordem_de_chegada.append(piloto)
            
            mostrar_corrida(pilotos, cores, posicoes, destino, maior_nome)
            
            printar_cabecalho("Chegadas:")
            for i in range(len(ordem_de_chegada)):
                print(f"{i + 1} Lugar: {ordem_de_chegada[i]}")
        time.sleep(0.5 * velocidade)
    return ordem_de_chegada
