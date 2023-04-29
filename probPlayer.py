import itertools
from typing import Dict, List, Tuple

import probabilidade
import combinacao


def soma_valida(hand: int, target: int, permutation: Tuple[int]) -> bool:

    total = hand
    for carta in permutation:
        if carta == 1 and total < 11:
            total += 10
        total += carta 
        if total >  20 and total != target:
            return False
    return True

def permutacao(minha_mao: int, valor_desejado: int, DICIONARIO: Dict[int, int]) -> Tuple[List[int], int]:

    for comb_base in combinacao.comb(minha_mao, valor_desejado, DICIONARIO):
        quantidade = 0
        for perm in set(itertools.permutations(comb_base, len(comb_base))):
            if(probabilidade.perm_valida(minha_mao, comb_base, perm)):
                #if(valor_desejado > 21):
                  #  if(soma_valida(minha_mao, valor_desejado, perm)):
                        #print(perm)
                  #      quantidade += 1
                #else:
                    #print(perm)
                    #quantidade += 1
                quantidade += 1
        if quantidade != 0:
            print(comb_base, quantidade)
            yield comb_base, quantidade




def probabilidade_comb(comb_base: List[int], quantidade: int, DICIONARIO: Dict[int, int]) -> float:
    if quantidade != 0:
        prob = 1
        total_cartas = probabilidade.quantidade_cartas_baralho(DICIONARIO)
        baralho_copia = DICIONARIO.copy()
        for item in comb_base:
            if baralho_copia[item] > 0:
                prob *= baralho_copia[item]/total_cartas
                baralho_copia[item] -= 1
                total_cartas -= 1
        return prob * quantidade
    return

