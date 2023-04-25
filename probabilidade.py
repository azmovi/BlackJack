
def quantidade_cartas_baralho(DICIONARIO):

    soma = 0
    for key in DICIONARIO.keys():
        soma += DICIONARIO[key]
    return soma


def minha_soma(DICIONARIO):

    soma = 0
    items = list(DICIONARIO.items())
    print(items)
    for key, value in items[1:]:
        soma += key * value
    if(items[0][1]):
        if((soma + 11) <= 21):
            soma += 11
        else:
            soma += 1
    return soma

def lista_soma(total, minha_mao, indice):

    if(indice == 1 and (total + minha_mao) < 11):
        return total + 11
    else:
        return total + indice

def soma_perm(minha_mao, perm):
    soma = minha_mao
    for item in perm:
        if(item == 1 and soma < 11):
            soma += 10
        soma += item
    return soma


def perm_valida(minha_mao, perm_base, perm_nova):
    if(soma_perm(minha_mao, perm_base) != soma_perm(minha_mao, perm_nova)):
        return False
    return True


