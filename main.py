import probabilidade
import os
from typing import List


global BARALHO 
BARALHO = [0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 16]
PLAYER = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
DEALER = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def quantidade_de_baralhos():
    global BARALHO
    n = int(input("Quantos Baralhos -> "))
    BARALHO = [item * n for item in BARALHO]
    return 


def retirou_carta_do_baralho(deck: List[int], hand: List[int], carta:int):
    """  """
    deck[carta] -= 1
    hand[carta] += 1
    return 

def player_jogada():
    """  """
    carta = int(input("Player-> "))
    retirou_carta_do_baralho(BARALHO, PLAYER, carta)
    return


def dealer_jogada():
    """  """
    carta = int(input("Dealer-> "))
    retirou_carta_do_baralho(BARALHO, DEALER, carta)
    return


def jogada_inicial():
    """  """
    player_jogada()
    player_jogada()
    dealer_jogada()
    return


def reseta_mao(deck: List[int]):
    """  """
    for i in range(len(deck)):
        deck[i] = 0
    return 

def novo_jogo():

    try:
        os.system("clear")
    except:
        os.system("cls")

    reseta_mao(PLAYER)
    reseta_mao(DEALER)
    jogada_inicial()
    return


def continuar_jogando():

    print("Player[0] - Dealer[1]")
    opt = int(input("> "))

    try:
        os.system("clear")
    except:
        os.system("cls")

    if(opt):
        dealer_jogada()

    else:
        player_jogada()

    return


def escolha_de_jogo():
    """  """
    print("Continuar[0] - NovoJogo[1] - Sair[2]")
    opt = int(input("> "))
    if(opt == 0):
        continuar_jogando()

    elif(opt == 1):
        novo_jogo()

    else:
        return False

    return True

def valor_mao(hand: List[int]) -> int:
    """  """
    soma = 0
    for i in range(len(hand)):
        soma += hand[i] * i
    return soma

def best_visu(lista_de_prob: List[float]):
    """  """
    indice = 17
    for prob in lista_de_prob:
        print(indice, "->", prob)
        indice += 1

def minha_mao(hand: int):
    indice = 0
    mao = []
    for item in hand:
        if(indice):
            for i in range(item):
                mao.append(indice)
        indice += 1
    print(mao)


def show():
    """  """
    print("-------------------BARALHO--------------")
    print(BARALHO)
    print()

    print("-----------------PLAYER----------------") #1 
    print("MÃO->", end="")
    minha_mao(PLAYER)
    hand = valor_mao(PLAYER)
    probabilidade.show_probabilidade(hand, BARALHO, 1)

    print("----------------DEALER-------------") #0
    print("MÃO->", end="")
    minha_mao(DEALER)
    hand = valor_mao(DEALER)
    probabilidade.show_probabilidade(hand, BARALHO, 0)
    print()
    return

def inicio_de_jogo():

    quantidade_de_baralhos()
    show()
    jogada_inicial()
    return
    


def main():
    inicio_de_jogo()
    game = True
    while(game == True):
        show()
        game = escolha_de_jogo()
    return


main()
