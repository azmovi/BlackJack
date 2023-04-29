import combinacao
import probabilidade
import itertools



def soma_valida(minha_mao: int, valor_desejado: int, perm: list[int]) -> bool:
    soma = minha_mao
    for item in perm:
        if((item == 1) and soma < 11):
            soma += 10
        soma += item
        if(soma > 16 and soma != valor_desejado):
            return False
    return True

def permutacao(minha_mao: int, valor_desejado:int, DICIONARIO: dict[int, int]) -> list[tuple[int], int]:

    for comb_base in combinacao.comb(minha_mao, valor_desejado, DICIONARIO):
        quantidade = 0
        for perm in set(itertools.permutations(comb_base, len(comb_base))):
            if(probabilidade.perm_valida(minha_mao, comb_base, perm)):
                if(valor_desejado > 16):
                    if(soma_valida(minha_mao, valor_desejado, perm)):
                        #print(perm)
                        quantidade += 1
                else:
                    #print(perm)
                    quantidade += 1
        yield comb_base, quantidade

def probabilidade_comb(comb_base: list[int], quantidade: int, DICIONARIO: dict[int, int]) -> float:
    total_cartas = probabilidade.quantidade_cartas_baralho(DICIONARIO)
    prob = 1
    baralho_copia = DICIONARIO.copy()
    for item in comb_base:
        if baralho_copia[item] > 0:
            prob *= baralho_copia[item]/total_cartas
            baralho_copia[item] -= 1
            total_cartas -= 1
    return prob * quantidade
