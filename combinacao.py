from typing import Tuple, List


def combinacao(
    minha_mao: int, valor_desejado: int, baralho: List
) -> List[List[int]]:
    """ """
    all_comb = []
    target = valor_desejado - minha_mao

    def dfs(indice: int, comb: List[int], total: int):
        if total == target:
            all_comb.append(comb.copy())
            return

        if indice < 0 or total > target:
            return

        if baralho[indice] == 0:
            dfs(indice - 1, comb, total)
            return

        comb.append(indice) 
        baralho[indice] -= 1

        dfs(
            indice,
            comb,
            soma_comb(total, minha_mao, indice)
        )   # total + indice

        comb.pop()
        baralho[indice] += 1
        dfs(indice - 1, comb, total)

    dfs(10, [], 0)
    return all_comb


def permutacao(
    hand: int, valor_desejado: int, combinacao: List[int], usuario: int
) -> List[List[int]]:
    """ """
    all_perm = []
    contador = {}
    perm = []

    global quantidade
    quantidade = 0

    for key in combinacao:
        if key in contador:
            contador[key] += 1
        else:
            contador[key] = 1

    def dfs():
        """ """
        global quantidade

        if len(perm) == len(combinacao): 
            #all_perm.append(perm.copy())
            quantidade += 1
            return

        for key in contador:
            if contador[key] > 0 and valida_perm(
                hand, valor_desejado, perm, usuario):

                perm.append(key)
                contador[key] -= 1

                dfs()

                contador[key] += 1
                perm.pop()

    dfs()
    #print(all_perm)
    return quantidade
    #return all_perm


def valida_perm(
    hand: int, valor_desejado: int, perm: List[int], usuario: int
) -> int:
    soma = hand
    for numero in perm:
        if numero == 1 and soma < 11:
            soma += 10
        soma += numero
        if usuario:# Player
            if soma > 16 and soma != valor_desejado:
                return False
        else:# Dealer
            if soma > 16 and soma != valor_desejado:
                return False
    return True

def soma_comb(total: int, minha_mao: int, novo_valor: int) -> int:
    if novo_valor == 1 and (total + minha_mao) < 11:
        return total + 11
    else:
        return total + novo_valor 


def combinacao_e_numero_de_permutacoes(
    hand: int, wish: int, deck: List[int], usuario: int
) -> Tuple[List[int], int]:
    """ """
    for comb in combinacao(hand, wish, deck):
        quantidade =  permutacao(hand, wish, comb, usuario)
        if quantidade != 0:
            yield comb, quantidade
    return

