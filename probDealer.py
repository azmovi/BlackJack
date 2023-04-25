import combinacao
import probabilidade
import itertools

BARALHO = {1: 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 4, 8: 4, 9: 4, 10: 16}

def n_baralho(n):
    for key, value in BARALHO.items():
        BARALHO[key] = value * n
    return

def permutacao(minha_mao, valor_desejado, DICIONARIO):

    for comb_base in combinacao.comb(minha_mao, valor_desejado, DICIONARIO):
        quantidade = 0
        for perm in set(itertools.permutations(comb_base, len(comb_base))):
            if(probabilidade.perm_valida(minha_mao, comb_base, perm)):
                quantidade += 1
        yield comb_base, quantidade

def probabilidade_comb(comb_base, quantidade, DICIONARIO):
    total_cartas = probabilidade.quantidade_cartas_baralho(DICIONARIO.copy())
    prob = 1
    baralho_copia = DICIONARIO.copy()
    print(comb_base)
    for item in comb_base:
        if baralho_copia[item] > 0:
            prob *= baralho_copia[item]/total_cartas
            baralho_copia[item] -= 1
            total_cartas -= 1
    print(prob * quantidade)
    return prob * quantidade

def main():
    prob_total = 0
    for comb_base, quantidade in permutacao(14, 16, BARALHO):
        prob_total += probabilidade_comb(comb_base, quantidade, BARALHO)
    print(round(prob_total * 100, 3))
    return
main()

