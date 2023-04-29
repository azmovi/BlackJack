import probPlayer
import probDealer

from numba import jit


BARALHO = {1: 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 4, 8: 4, 9: 4, 10: 16}


def mostra_probabilidade(minha_mao, usuario):

    print("Minha mão = ", minha_mao)
    prob_safe= 0
    prob_burst = 0

    if(usuario):
        for i in range(minha_mao + 1, 27):
            prob_valor= 0
            for comb_base, quantidade  in probPlayer.permutacao(minha_mao, i, BARALHO):
                prob_valor+= probPlayer.probabilidade_comb(comb_base, quantidade, BARALHO)
            print("Chegar=", i, "->", round(prob_valor* 100, 3))
            print()
            if(i < 22):
                prob_safe += prob_valor
            else:
                prob_burst += prob_valor


    else:
        for i in range(minha_mao + 1, 27):
            prob_valor= 0
            for comb_base, quantidade  in probDealer.permutacao(minha_mao, i, BARALHO):
                prob_valor+= probDealer.probabilidade_comb(comb_base, quantidade, BARALHO)
            print("Chegar=", i, "->", round(prob_valor* 100, 3))
            print()
            if(i < 22):
                prob_safe += prob_valor
            else:
                prob_burst += prob_valor

    return round(prob_safe * 100, 3), round(prob_burst * 100, 3)

def teste_probabilidade(minha_mao, valor_desejado, usuario):
    prob_valor = 0
    if(usuario):
        for comb_base, quantidade  in probPlayer.permutacao(minha_mao, valor_desejado, BARALHO):
            prob_valor += probPlayer.probabilidade_comb(comb_base, quantidade, BARALHO)
    else:
        for comb_base, quantidade  in probDealer.permutacao(minha_mao, valor_desejado, BARALHO):
            prob_valor += probDealer.probabilidade_comb(comb_base, quantidade, BARALHO)


    return round(prob_valor * 100, 3)

def n_baralhos(n):
    for key, value in BARALHO.items():
        BARALHO[key] = value * n
    return

def main():
    #safe, dar_merda = mostra_probabilidade(15, 0)
    #print(safe, dar_merda)
    print(teste_probabilidade(10, 21, 1))
    print()
    return

main()
