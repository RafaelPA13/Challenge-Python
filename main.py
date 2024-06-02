import game
from funcoes import *

EQUIPES = [
    "Porsche",
    "Jaguar",
    "MCLaren",
    "Andretti",
    "Nissan",
    "Mahindra",
    "Maseratti",
]

PILOTOS = [
    "Antonio Felix",
    "Nick Cassidy",
    "Oliver Rowland"
    "Sam Bird",
    "Edoardo Mortara",
    "Maximilian Günther"
]

PILOTOS_EQUIPES = [
    "Porsche",
    "Jaguar",
    "Nissan",
    "MCLaren",
    "Mahindra",
    "Maseratti"
]


numero_de_podios = 3

podios = []

printar_cabecalho("Bem vindo ao Cartola Formula-E!")

while True:
    print(f"Escolha os pilotos para o podio de hoje:")
    printar_opcoes(PILOTOS)
    
    while len(podios) < numero_de_podios:
        piloto = escolher_opcao_index(f"Por favor, digite o número do piloto para o {len(podios) + 1} Podio: ", PILOTOS)
        
        if piloto in podios:
            print("Piloto ja escolhido.")
            continue

        podios.append(piloto)

    print("Os pilotos escolhidos foram:")
    for i in range(len(podios)):
        print(f"{i + 1} Podio: {PILOTOS[podios[i]]}")
    
    confirma = escolher_opcao("Deseja confirmar os pilotos escolhidos? (s/n): ", ["s", "n"])

    if confirma == "s":
        break
    else:
        podios = []

limpar_terminal()

melhor_equipe = ""

while True:
    printar_cabecalho("Escolha a equipe que fará mais pontos")
    printar_opcoes(EQUIPES)

    melhor_equipe = escolher_opcao_index("Digite o número da equipe: ", EQUIPES)

    print(f"A equipe escolhida que fará mais pontos será: {EQUIPES[melhor_equipe]}")

    confirma = escolher_opcao("Deseja confirmar a equipe escolhida? (s/n): ", ["s", "n"])

    if confirma == "s":
        break


limpar_terminal()

printar_cabecalho("Suas apostas")
print("Podios:")
for i in range(len(podios)):
    print(f"{i + 1} Podio: {PILOTOS[podios[i]]}")

printar_linha()

print(f"Melhor Equipe: {EQUIPES[melhor_equipe]}")

printar_cabecalho("A corrida vai começar! Boa sorte aos pilotos!")

ordem_de_chegada = game.iniciar_corrida(PILOTOS)

pontos_equipes = [0] * len(PILOTOS_EQUIPES)

for i in range(len(ordem_de_chegada)):
    pilotoIndex = PILOTOS.index(ordem_de_chegada[i])
    equipeIndex = pilotoIndex
    pontos_equipes[equipeIndex] += (len(ordem_de_chegada) - i) * 10

printar_cabecalho("Pontuacao das equipes")
equipe_vencedora = 0
for equipeIndex in range(len(PILOTOS_EQUIPES)):
    print(f"{PILOTOS_EQUIPES[equipeIndex]}: {pontos_equipes[equipeIndex]} pontos")
    if pontos_equipes[equipeIndex] > pontos_equipes[equipe_vencedora]: # Escolhe a equipe com mais pontos
        equipe_vencedora = equipeIndex


printar_cabecalho("Resultados")

print("Podios:")
for i in range(len(podios)):
    piloto_escolhido = PILOTOS[podios[i]]

    acertouAposta = ordem_de_chegada[i] == piloto_escolhido

    mensagem = f"{i + 1} Podio: {ordem_de_chegada[i]}, seu palpite: {piloto_escolhido} - "
    if acertouAposta:
        mensagem += "Acertou!"
    else:
        mensagem += "Errou!"

    print(mensagem)

printar_linha()
acertouMelhorEquipe = PILOTOS_EQUIPES[melhor_equipe] == PILOTOS_EQUIPES[equipe_vencedora]

mensagem = f"Melhor Equipe: {PILOTOS_EQUIPES[equipe_vencedora]}, seu palpite: {PILOTOS_EQUIPES[melhor_equipe]} - "
if acertouMelhorEquipe:
    mensagem += "Acertou!"
else:
    mensagem += "Errou!"

print(mensagem)