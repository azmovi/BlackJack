import probabilidade
from typing import List


global BARALHO 
global CONTAGEM
CONTAGEM = 0
BARALHO = [0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 16]
PLAYER = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
DEALER = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
LIXO = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


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
    global CONTAGEM
    pede = True
    while(pede):
        carta = int(input("Player-> "))
        if(carta == 0):
            pede = False
        else:
            retirou_carta_do_baralho(BARALHO, PLAYER, carta)
            CONTAGEM += contagem(carta)
    return


def dealer_jogada():
    """  """
    global CONTAGEM
    pede = True
    while(pede):
        carta = int(input("Dealer-> "))
        if(carta == 0):
            pede = False
        else:
            retirou_carta_do_baralho(BARALHO, DEALER, carta)
            CONTAGEM += contagem(carta)
    return


def lixo_jogada():
    """  """
    global CONTAGEM
    pede = True
    while(pede):
        carta = int(input("Outro-> "))
        if(carta == 0):
            pede = False
        else:
            retirou_carta_do_baralho(BARALHO, LIXO, carta)
            CONTAGEM += contagem(carta)
    return


def jogada_padrao():
    """  """
    player_jogada()
    lixo_jogada()
    dealer_jogada()
    return


def reseta_mao(deck: List[int]):
    """  """
    for i in range(len(deck)):
        deck[i] = 0
    return 


def novo_jogo():
    """  """
    reseta_mao(PLAYER)
    reseta_mao(DEALER)
    show()
    jogada_padrao()
    return



def escolha_de_jogo():
    """  """
    show()
    print("Continuar[0] - NovoJogo[1] - Sair[2]")
    opt = int(input("> "))
    if(opt == 0):
        jogada_padrao()

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

def contagem(carta: int) -> int:
    mais_um = [2, 3, 4, 5, 6]
    menos_um = [1, 10]
    if carta in mais_um:
        return 1
    if carta in menos_um:
        return -1
    return 0

def blackjack():
    total_cartas = sum(BARALHO)
    prob_as = BARALHO[1]/total_cartas
    prob_dez = BARALHO[10]/total_cartas
    print(round(prob_as * prob_dez * 2 * 100, 2))
    return

def tirar_dez():
    return round(BARALHO[10]/sum(BARALHO) * 100, 2)

def show():
    """  """
    print("-----------------BARALHO---------------")
    print(BARALHO[1:])
    print()

    print("-----------------PLAYER----------------") #1 
    print("MÃO->", end="")
    minha_mao(PLAYER)
    hand = valor_mao(PLAYER)
    probabilidade.show_probabilidade(hand, BARALHO, 1)

    print("-----------------DEALER----------------") #0
    print("MÃO->", end="")
    minha_mao(DEALER)
    hand = valor_mao(DEALER)
    probabilidade.show_probabilidade(hand, BARALHO, 0)
    print("---------------------------------------")
    print("CONTAGEM->", CONTAGEM)
    print("BLACKJACK-> ", end="")
    blackjack()
    print("DEZ->", tirar_dez())
    print()
    return

def inicio_de_jogo():

    quantidade_de_baralhos()
    show()
    jogada_padrao()
    return
    


def main():
    inicio_de_jogo()
    game = True
    while(game == True):
        game = escolha_de_jogo()
    return


main()
