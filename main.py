import probabilidade
import os


BARALHO = {1: 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 4, 8: 4, 9: 4, 10: 16}
DEALER = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
PLAYER = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}


def quantidade_de_baralhos():

    qt = int(input("Quantos Baralhos -> "))
    for key, value in BARALHO.items():
        BARALHO[key] = value * qt
    return 


def retirou_carta_do_baralho(DICIONARIO, carta):

   DICIONARIO[carta] += 1
   BARALHO[carta] -= 1
   return


def player_jogada():

    carta = int(input("Player-> "))
    retirou_carta_do_baralho(PLAYER, carta)
    return


def dealer_jogada():
    carta = int(input("Dealer-> "))
    retirou_carta_do_baralho(DEALER, carta)
    return


def jogada_inicial():

    player_jogada()
    player_jogada()
    dealer_jogada()
    return


def reseta_mao(DICIONARIO):

    for key in DICIONARIO.keys():
        DICIONARIO[key] = 0
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

    print("Continuar[0] - NovoJogo[1] - Sair[2]")
    opt = int(input("> "))
    if(opt == 0):
        continuar_jogando()

    elif(opt == 1):
        novo_jogo()

    else:
        return False

    return True



def main():

    quantidade_de_baralhos()
    jogada_inicial()
    
    game = True
    while(game == True):
        print(probabilidade.minha_soma(PLAYER))
        game = escolha_de_jogo()
    return


main()
