import probabilidade

def comb(minha_mao, quero_chegar, dicionario):
    all_comb = []
    target = quero_chegar - minha_mao

    def dfs(indice, comb, total):
        if(total == target):
            all_comb.append(comb.copy())
            return

        if(indice <= 0 or total > target):
            return

        if (dicionario[indice] == 0):
            dfs(indice - 1, comb, total)
            return
        
        comb.append(indice)
        dicionario[indice] -= 1
        dfs(indice, comb, probabilidade.lista_soma(total, minha_mao, indice)) # total + indice
        comb.pop()
        dicionario[indice] += 1
        dfs(indice - 1, comb, total)

    dfs(10, [], 0)
    return all_comb




