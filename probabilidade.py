import combinacao
from typing import List



def probabilidade_do_valor_desejado(
    hand: int, wish: int, deck: List[int], usuario: int
) -> int:
    """  """
    prob_total = 0
    for item in combinacao.combinacao_e_numero_de_permutacoes(hand, wish, deck, usuario):
        prob_total += probabilidade_comb(item[0], deck) * item[1] 
    return round(prob_total * 100, 2)



def probabilidade_comb(comb: List[int], deck: List[int]) -> int:
    """  """
    deck_copia = deck.copy()
    total_cartas = sum(deck)
    probabilidade = 1
    for indice in comb:
        if deck_copia[indice] > 0:
            probabilidade *= deck_copia[indice] / total_cartas
            deck_copia[indice] -= 1
            total_cartas -= 1
    return probabilidade


def probabilidade_burst_ou_vitoria(
    hand: int, deck: List[int], usuario: int, metodo: int
) -> List[float]:
    """  """
    lista_de_probabilidades = []

    if(metodo): # safe
        for wish in range(17, 22):
            lista_de_probabilidades.append(
                probabilidade_do_valor_desejado(hand, wish, deck, usuario)
            )

    else: # burst
        for wish in range(22, 27):
            lista_de_probabilidades.append(
                probabilidade_do_valor_desejado(hand, wish, deck, usuario)
            )
    return lista_de_probabilidades 

def show_probabilidade(hand: int, deck: List[int], usuario: int):
    """  """
    indice = 17
    victory = probabilidade_burst_ou_vitoria(hand, deck, usuario, 1)
    derrota = probabilidade_burst_ou_vitoria(hand, deck, usuario, 0)
    for item in victory:
        print(indice, "->", item)
        indice += 1

    print("VICTORY-> ", round(sum(victory), 2))
    print("BURST-> ", round(sum(derrota), 2))
    return

